import os
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description='vsi2tif - simple tool for converting images from cellSens VSI to Generic TIFF')
    parser.add_argument("input", help="folder with input files")
    parser.add_argument("output", help="folder for output files")
    parser.add_argument("--compression", help="compression technique used for last conversion step", default="jpeg")
    parser.add_argument("--plane", help="which image plane to convert image from - 0 is full resolution", default=0)
    parser.add_argument("--tilesize", help="tile size to use during both conversion steps", default=1024)
    parser.add_argument("--quality", help="compression quality used with JPEG compression", default=85)
    parser.add_argument("--bfconvert", help="path to bfconvert executable")
    argv = parser.parse_args()
    
    if not os.path.isfile(argv.bfconvert):
        raise FileNotFoundError(f"bfconvert not found at: {argv.bfconvert}")


if __name__ == '__main__':
    main()
