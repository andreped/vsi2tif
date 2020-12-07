# vsi2tif
Simple method for converting the CellSens .vsi format to a pyramidal .tif.

## Requirements (tested with Ubuntu 18.04 desktop)
### Python 3.*

pyvips

### Command line tools
vips (https://zoomadmin.com/HowToInstall/UbuntuPackage/libvips)\
install what comes with ubuntu:
apt install libvips-tools

bftools
https://docs.openmicroscopy.org/bio-formats/6.5.1/users/comlinetools/# (needs a JRE)

## How to use
Before you run the script, be sure to install all requirements. Also, as you are using a JVM, it might be smart to set the defaults in the script to your needs - like memory limit, e.g:

```python
input_file_type = 'vsi'
path_to_bfconvert = '../bftools/bfconvert'
java_env_var = {'BF_MAX_MEM': '4g'}
defaults = {
    'compression': 'lzw',
    'plane': 0,
    'tilesize': 1024,
    'quality': 85
}
```

If you see the example code, it requires that the path to bfconvert (from bftools) is predefined. The code includes some hard-coded hyperparamters which I have found to work well in my setup. This code is only meant to show a proof of concept. Feel free to adjust the code as you please.

### CLI usage
usage:
```
vsi2tif.py [-h] [--compression COMPRESSION] [--plane PLANE] [--tilesize TILESIZE] [--quality QUALITY] [--keep_tmp_files] input output

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

#### some additional info

* script runs currently single threaded - not very fast for larger batches
* info on processed files will be stored in one json `processed_files_info.json` in the output folder
