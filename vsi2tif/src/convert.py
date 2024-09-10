import logging
import os
from tempfile import TemporaryDirectory

from .utils import run_wrapper


def cellsens2raw(
    input_path: str,
    output_path: str,
    bfconvert: str,
    compression: str = "LZW",
    tz: int = 1024,
    plane: int = 0,
    max_mem: int = 32,
    verbose: int = 1,
) -> None:
    if not os.path.exists(bfconvert):
        raise FileNotFoundError(f"bfconvert not found at: {bfconvert}")
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found at: {input_path}")

    cmd = (
        f"{bfconvert} -tilex {tz} -tiley {tz} -nogroup -no-upgrade -overwrite -bigtiff -series {plane} "
        f'-compression {compression} "{input_path}" "{output_path}"'
    )
    try:
        run_wrapper(cmd=cmd, verbose=verbose, max_mem=max_mem)
    except RuntimeError as e:
        logging.error(e)


def raw2tif(input_path: str, output_path: str, compression: str = "jpeg", quality: int = 85, verbose: int = 1) -> None:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found at: {input_path}")

    os.makedirs("/".join(output_path.split("/")[:-1]), exist_ok=True)

    cmd = (
        f'vips tiffsave "{input_path}" "{output_path}" --bigtiff --tile --pyramid --compression={compression}'
        f" --Q={quality}"
    )
    try:
        run_wrapper(cmd=cmd, verbose=verbose)
    except RuntimeError as e:
        logging.error(e)


def cellsens2tif(
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
    # create temporary directory to store intermediate files
    with TemporaryDirectory() as temp_dir:
        # create temporary path for raw TIFF
        bigtiff_path = os.path.join(temp_dir, "temporary.btf")

        # first convert from Olympus format to raw TIFF
        try:
            cellsens2raw(input_path, bigtiff_path, bfconvert, "LZW", tz, plane, max_mem, verbose)
        except Exception as e:
            logging.error(f"Failed to convert Olympus file to BigTIFF. Skipping image: {input_path}")
            raise e

        # construct tiled, pyramidal TIFF
        try:
            raw2tif(bigtiff_path, output_path, compression, quality, verbose)
        except Exception as e:
            logging.error(f"Failed to convert BigTIFF to tiled, pyramidal TIFF. Skipping image: {input_path}")
            logging.error(e)
            raise e
