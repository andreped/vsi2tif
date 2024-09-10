import os
import traceback
import shutil
from tqdm import tqdm

from .benchmark import benchmark
from .convert import cellsens2tif


@benchmark
def cellsens2tif_single(
    input_path: str,
    output_path: str,
    bfconvert: str,
    compression: str = "jpeg",
    tz: int = 1024,
    plane: int = 0,
    quality: int = 85,
    max_mem: int = 32,
    verbose: int = 1,
) -> None:

    if int(plane) == -1:
        image_folder = os.path.join(os.path.dirname(output_path), os.path.basename(output_path).replace('.tif', ''))
        for s in range(50):
            try:
                curr_output_path = os.path.join(image_folder, "plane_" + str(s) + "_" + os.path.basename(output_path))
                cellsens2tif(input_path, curr_output_path, bfconvert, compression, tz, s, quality, max_mem, verbose)
            except Exception as e:
                logging.info("End of planes with value {}".format(s))
                break

        try:
            largest_size = 0
            largest_file = None
            for _, _, files in os.walk(image_folder):
                for f in files:
                    fp = os.path.join(image_folder, f)
                    fs = os.path.getsize(fp)
                    if fs > largest_size:
                        largest_size = fs
                        largest_file = fp
            shutil.copyfile(largest_file, output_path)
            if os.path.exists(image_folder):
                shutil.rmtree(image_folder)
        except Exception as e:
            logging.error("Issue cleaning up after all planes conversion.")
            logging.error(traceback.format_exc())
    else:
        cellsens2tif(input_path, output_path, bfconvert, compression, tz, plane, quality, max_mem, verbose)


@benchmark
def cellsens2tif_batch(
    input_path: str,
    output_path: str,
    bfconvert: str,
    compression: str = "jpeg",
    tz: int = 1024,
    plane: int = 0,
    quality: int = 85,
    max_mem: int = 32,
    verbose: int = 1,
) -> None:
    # create directory if it does not exist
    os.makedirs(output_path, exist_ok=True)

    # find path to all cellSens VSI images to convert
    paths = []
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.lower().endswith("overview.vsi"):
                continue
            if file.endswith(".vsi"):
                paths.append((root, file))

    # perform conversion in separate processes
    for root, file in tqdm(paths):
        curr_input_path = os.path.join(root, file)
        curr_output_path = (output_path + "/" + curr_input_path.split(input_path)[-1]).replace(".vsi", ".tif")

        try:
            cellsens2tif_single(
                curr_input_path, curr_output_path, bfconvert, compression, tz, plane, quality, max_mem, verbose
            )
        except Exception:
            continue
