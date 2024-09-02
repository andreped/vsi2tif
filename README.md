# vsi2tif

Tool for converting WSIs from Olympus' cellSens VSI to Generic TIFF.

## Requirements

To run the tool, you need to configure bftools and vips. To do that, follow the instructions below for the operating system of interest:

<details>
<summary>

### Ubuntu</summary>

1. Download bftools (click [here](http://downloads.openmicroscopy.org/latest/bio-formats5.6/artifacts/bftools.zip))

2. Install vips and JDK
```
sudo apt update
sudo apt-get install openjdk-8-jdk
sudo apt install libvips-tools
```

</details>


<details>
<summary>

### macOS</summary>

1. Download bftools (click [here](http://downloads.openmicroscopy.org/latest/bio-formats5.6/artifacts/bftools.zip))

2. Install vips and JDK
```
brew install --cask zulu@8
brew install vips
```

</details>


## Installation

Install from source:
```
pip install git+https://github.com/andreped/vsi2tif
```

## Usage

The conversion tool is available through a command line interface (CLI).

Example for converting a single WSI:
```
vsi2tif -i /path/to/olympus/image.vsi -o /path/to/converted/image.tif -b /path/to/bftools/bfconvert
```

Here is an example to perform batch conversion of a folder of WSIs:
```
vsi2tif -i /path/to/olympus/wsis/ -o /path/to/converted/wsis/directory/ -b /path/to/bftools/bfconvert
```

Comprehensive CLI documentation can be seen below:

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
