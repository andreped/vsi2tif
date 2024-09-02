import os

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
    paths = [(root, file) for root, _, files in os.walk(input_path) for file in files if file.endswith(".vsi")]

    # perform conversion in separate processes
    for root, file in tqdm(paths):
        curr_input_path = os.path.join(root, file)
        curr_output_path = os.path.join(output_path, output_path.split(root)[0], file).replace(".vsi", ".tif")

        cellsens2tif(curr_input_path, curr_output_path, bfconvert, compression, tz, plane, quality, max_mem, verbose)
