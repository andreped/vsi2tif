import logging
import os
import subprocess as sp


def run_wrapper(cmd: str, verbose: int = 0, max_mem: int = 4):
    # merge current environment with the new BF_MAX_MEM variable
    env = os.environ.copy()
    env["BF_MAX_MEM"] = f"{max_mem}g"

    if verbose == 0:
        # capture the output silently when verbose is disabled
        result = sp.run(cmd, shell=True, env=env, capture_output=True, text=True)

        # check if the process failed
        if result.returncode != 0:
            raise RuntimeError(f"Command failed with error: {result.stderr}")

    else:
        # stream output in real-time if verbose is enabled
        process = sp.Popen(cmd, shell=True, env=env, stdout=sp.PIPE, stderr=sp.PIPE, text=True)

        # stream stdout in real-time
        for stdout_line in iter(process.stdout.readline, ""):
            logging.info(stdout_line.strip())  # Log each line of output
        process.stdout.close()

        # wait for process to finish
        process.wait()

        # check if the process failed
        if process.returncode != 0:
            stderr_output = process.stderr.read().strip()
            process.stderr.close()
            raise RuntimeError(f"Command failed with error: {stderr_output}")

        process.stderr.close()
