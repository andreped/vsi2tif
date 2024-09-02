# vsi2tif

Tool for converting WSIs from Olympus' cellSens VSI to Generic TIFF.

## Installation

1. Download bftools (click [here](http://downloads.openmicroscopy.org/latest/bio-formats5.6/artifacts/bftools.zip))

2. Install vips and JDK
```
sudo apt update
sudo apt-get install openjdk-8-jdk
sudo apt install libvips-tools
```

3. Install `vsi2tif` CLI
```
pip install git+https://github.com/andreped/vsi2tif
```

## Usage

The conversion tool is available through a command line interface (CLI):

```
vsi2tif [-h] -i INPUT -o OUTPUT -b BFCONVERT [-c COMPRESSION] [-p PLANE] [-s TILESIZE] [-q QUALITY]

positional arguments:
  INPUT      folder with input files
  OUTPUT     folder for output files
  BFCONVERT  path to bfconvert tool

optional arguments:
  -h, --help                   show this help message and exit
  --compression COMPRESSION    compression technique used for last conversion step - default 'jpeg'
  --plane PLANE                which image plane to convert image from - default 0
  --tilesize TILESIZE          tile size to use during both conversion steps - default 1024
  --quality QUALITY            compression quality used with JPEG compression - default 85
```

## License

This project has [MIT license](https://github.com/andreped/vsi2tif/blob/main/LICENSE).
