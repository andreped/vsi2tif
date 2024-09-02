import os
from argparse import ArgumentParser

from .src.process import vsi2tif_batch
from .src.process import vsi2tif_single


def main():
    parser = ArgumentParser(description="vsi2tif - simple tool for converting images from cellSens VSI to Generic TIFF")
    parser.add_argument("-i", "--input", help="folder with input files", required=True)
    parser.add_argument("-o", "--output", help="folder for output files", required=True)
    parser.add_argument("-b", "--bfconvert", help="path to bfconvert tool", required=True)
    parser.add_argument("-c", "--compression", help="compression technique for final image", default="jpeg")
    parser.add_argument("-p", "--plane", help="which image plane to convert image from", default=0)
    parser.add_argument("-s", "--tilesize", help="tile size to use during both conversion steps", default=1024)
    parser.add_argument("-q", "--quality", help="compression quality used with JPEG compression", default=85)
    argv = parser.parse_args()

    if not os.path.isfile(argv.bfconvert):
        raise FileNotFoundError(f"bfconvert not found at: {argv.bfconvert}")
    if not os.path.exists(argv.input):
        raise FileNotFoundError(f"Input directory not found at: {argv.input}")

    os.makedirs(argv.output, exist_ok=True)

    if os.path.isdir(argv.input):
        vsi2tif_batch(
            argv.input, argv.output, argv.bfconvert, argv.compression, argv.tilesize, argv.plane, argv.quality
        )
    else:
        vsi2tif_single(
            argv.input, argv.output, argv.bfconvert, argv.compression, argv.tilesize, argv.plane, argv.quality
        )


if __name__ == "__main__":
    main()
