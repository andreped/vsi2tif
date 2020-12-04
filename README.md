# vsi2tif
Simple method for converting the CellSens .vsi format to a pyramidal .tif. See example script.

## Requirements (tested with Ubuntu 18.04 desktop)
### Python 3.*
javabridge==1.0.18\
python-bioformats==1.5.2\
pytictoc==1.5.0

### Command line tools
vips (https://zoomadmin.com/HowToInstall/UbuntuPackage/libvips)\
bftools (https://forum.image.sc/t/bfconvert-command-line-tool/5872/2)

Also, **javabridge** requires that the Java SDK is installed. Current version of java is (openjdk 11.0.4 2019-07-16).

## How to use
Before you run the script, be sure to install all requirements. Also, as you are using a JVM, it might be smart to set the memory limit, e.g:\
`
export BF_MAX_MEM=2g
`

If you see the example code, it requires that the path to bfconvert (from bftools) is predefined. The code includes some hard-coded hyperparamters which I have found to work well in my setup. This code is only meant to show a proof of concept. Feel free to adjust the code as you please.
