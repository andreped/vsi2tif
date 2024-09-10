import logging
import os
from argparse import ArgumentParser

from .src.process import cellsens2tif_batch
from .src.process import cellsens2tif_single


def main():
    parser = ArgumentParser(description="vsi2tif - simple tool for converting images from cellSens VSI to Generic TIFF")
    parser.add_argument("-i", "--input", help="folder with input files", required=True)
    parser.add_argument("-o", "--output", help="folder for output files", required=True)
    parser.add_argument("-b", "--bfconvert", help="path to bfconvert tool", required=True)
    parser.add_argument("-c", "--compression", help="compression technique for final image", default="jpeg")
    parser.add_argument("-s", "--tilesize", help="tile size to use during both conversion steps", default=1024)
    parser.add_argument("-p", "--plane", help="which image plane to convert image from. If set to -1, all planes are converted and the largest is kept", default=0, dtype=int)
    parser.add_argument("-q", "--quality", help="compression quality used with JPEG compression", default=85)
    parser.add_argument("-m", "--max-mem", help="set maximum memory in the java vm", default=32)
    parser.add_argument("-v", "--verbose", help="set verbosity level", default=1, type=int)
    argv = parser.parse_args()

    if argv.verbose not in list(range(6)):
        raise ValueError("Verbosity level must be an integer between 0 and 5")

    logging.getLogger().setLevel(argv.verbose)

    if not os.path.isfile(argv.bfconvert):
        raise FileNotFoundError(f"bfconvert not found at: {argv.bfconvert}")
    if not os.path.exists(argv.input):
        raise FileNotFoundError(f"Input directory not found at: {argv.input}")

    if os.path.isdir(argv.input):
        logging.info("Performing batch conversion...")
        cellsens2tif_batch(
            argv.input,
            argv.output,
            argv.bfconvert,
            argv.compression,
            argv.tilesize,
            argv.plane,
            argv.quality,
            argv.max_mem,
            argv.verbose,
        )
    else:
        logging.info("Performing single conversion...")
        cellsens2tif_single(
            argv.input,
            argv.output,
            argv.bfconvert,
            argv.compression,
            argv.tilesize,
            argv.plane,
            argv.quality,
            argv.max_mem,
            argv.verbose,
        )


if __name__ == "__main__":
    main()
