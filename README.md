# vsi2tif

Tool for converting WSIs from Olympus' cellSens VSI to Generic TIFF.

## Requirements

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

## Getting Started

The conversion tool is available through a command line interface (CLI):

```
vsi2tif [-h] [--compression COMPRESSION] [--plane PLANE] [--tilesize TILESIZE] [--quality QUALITY] [--keep_tmp_files] input output

positional arguments:
  input      folder with input files
  output     folder for output files

optional arguments:
  -h, --help            show this help message and exit
  --compression COMPRESSION
                        Compression to use for tiff - default lzw - use something that is compatible with bfconvert and libvips - no checks implemented
                        yet!
  --plane PLANE         Plane to use from VSI - default 0
  --tilesize TILESIZE   Tilesize to use during conversion and in final image - default 1024
  --quality QUALITY     Quality value for (if used by compression) final image - default 85
  --keep_tmp_files      If given files from vsi to bigtiff conversion won't be deleted
```

## License

This project has [MIT license](https://github.com/andreped/vsi2tif/blob/main/LICENSE).
