# [vsi2tif](https://github.com/andreped/vsi2tif#vsi2tif)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Pip Downloads](https://img.shields.io/pypi/dm/vsi2tif?label=pip%20downloads&logo=python)](https://pypi.org/project/vsi2tif/)
[![PyPI version](https://badge.fury.io/py/vsi2tif.svg)](https://badge.fury.io/py/vsi2tif)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13745169.svg)](https://doi.org/10.5281/zenodo.13745169)
<a href="https://colab.research.google.com/gist/andreped/0e945c30ebb01b309a36162d9ec133ae/vsi2tif-converting-olympus-wsi-to-generic-tiff-ubuntu-linux.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Tool for converting WSIs from Olympus' cellSens VSI to Generic TIFF.

To quickly get started, see these notebooks ([Ubuntu Linux](https://github.com/andreped/vsi2tif/blob/main/notebooks/conversion_tutorial_ubuntu_linux.ipynb), [macOS](https://github.com/andreped/vsi2tif/blob/main/notebooks/conversion_tutorial_macos.ipynb)) for installing the tool, converting your first image, and verifying that the image works with OpenSlide.

## [Continuous integration](https://github.com/andreped/vsi2tif#continuous-integration)

| Build Type | Status |
| - | - |
| **Integration Tests** | [![CI](https://github.com/andreped/vsi2tif/workflows/Integration%20Tests/badge.svg)](https://github.com/andreped/vsi2tif/actions) |
| **Unit Tests** | [![CI](https://github.com/andreped/vsi2tif/workflows/Build%20Package/badge.svg)](https://github.com/andreped/vsi2tif/actions) |
| **Linting Checks** | [![CI](https://github.com/andreped/vsi2tif/workflows/Check%20Linting/badge.svg)](https://github.com/andreped/vsi2tif/actions) |

## [Requirements](https://github.com/andreped/vsi2tif#requirements)

To run the tool, you need to configure bftools and vips. To do that, follow the instructions below for the operating system of interest:

<details open>
<summary>

### [Ubuntu](https://github.com/andreped/vsi2tif#ubuntu)</summary>

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

### [macOS](https://github.com/andreped/vsi2tif#macos)</summary>

1. Download bftools (click [here](http://downloads.openmicroscopy.org/latest/bio-formats5.6/artifacts/bftools.zip))

2. Install vips and JDK
```
brew install --cask zulu@8
brew install vips
```

</details>

<details>
<summary>

### [Windows](https://github.com/andreped/vsi2tif#windows)</summary>

To install bftools and vips, I recommend using Powershell as much as possible to automate the installation steps.

1. Download bftools (click [here](http://downloads.openmicroscopy.org/latest/bio-formats5.6/artifacts/bftools.zip))

2. Download vips binary from Windows from [here](https://github.com/libvips/build-win64-mxe/releases) or use wget or similar
```
https://github.com/libvips/build-win64-mxe/releases/download/v8.15.3/vips-dev-w64-all-8.15.3.zip
```

3. Uncompress downloaded file and place it at an appropriate place, like at home
```
unzip ~/Downloads/vips-dev-w64-all-8.15.3.zip
mv ~/Downloads/vips-dev-w64-all-8.15.3/vips-dev-8.15/ ~/vips-dev-8.15/
```

4. Add path to `vips.exe` to the PATH (requires powershell administrator)
```
$Env:PATH += ";$HOME/vips-dev-8.15/bin/"
```

</details>


## [Installation](https://github.com/andreped/vsi2tif#installation)

Install from source:
```
pip install git+https://github.com/andreped/vsi2tif
```

## [Usage](https://github.com/andreped/vsi2tif#usage)

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
usage: vsi2tif [-h] -i INPUT -o OUTPUT -b BFCONVERT [-c COMPRESSION] [-s TILESIZE] [-q QUALITY] [-m MAX_MEM] [-v VERBOSE] [--remove-name-spaces] [-p PLANE] [--noskip-converted] [-f EXTENSION]

vsi2tif - simple tool for converting images from cellSens VSI to Generic TIFF

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        folder with input files
  -o OUTPUT, --output OUTPUT
                        folder for output files
  -b BFCONVERT, --bfconvert BFCONVERT
                        path to bfconvert tool
  -c COMPRESSION, --compression COMPRESSION
                        compression technique for final image - default 'jpeg'
  -s TILESIZE, --tilesize TILESIZE
                        tile size to use during both conversion steps - default 1024
  -q QUALITY, --quality QUALITY
                        compression quality used with JPEG compression - default 87
  -m MAX_MEM, --max-mem MAX_MEM
                        set maximum memory in the java vm - default 32
  -v VERBOSE, --verbose VERBOSE
                        set verbosity level - default 1
  --remove-name-spaces  replace spaces in filename with underscores in batch mode
  -p PLANE, --plane PLANE
                        image plane to convert image from. If set to -1, all series are converted and the largest is kept - default 0
  --noskip-converted    To specifically request existing files to be converted again
  -f EXTENSION, --extension EXTENSION
                        extension type to consider (e.g., .vsi)
```

## [License](https://github.com/andreped/vsi2tif#license)

This project has [MIT license](https://github.com/andreped/vsi2tif/blob/main/LICENSE).

## [How to cite](https://github.com/andreped/vsi2tif#how-to-cite) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13745169.svg)](https://doi.org/10.5281/zenodo.13745169)

If you found this tool useful in your research, please cite the following:
```
@software{pedersen2024vsi2tif,
  author       = {André Pedersen and David Bouget and Sebastian Krossa and Erik Smistad},
  title        = {{andreped/vsi2tif: v0.1.4}},
  month        = sep,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v0.1.4},
  doi          = {10.5281/zenodo.13745169},
  url          = {https://doi.org/10.5281/zenodo.13745169}
}
```