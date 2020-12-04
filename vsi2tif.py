import subprocess as sp
import os
from pytictoc import TicToc
import javabridge as jb
import bioformats as bf


# initialize timer
t = TicToc()
t.tic()

# choose image to convert
loc = "/mnt/EncryptedData2/pathology/images/126.vsi"

# output path
out_path = "/mnt/EncryptedPathology/pathology/sandbox/convert_test/"

# path to bfconvert command line tool
bfconvert_path = "/home/andrep/DP/python/bftools/bfconvert"

# set memory limit # <- DIDN'T WORK BETWEEN SUBPROCESSES(!)
#process = sp.Popen("export BF_MAX_MEM=0.2g".split(), stdout=sp.PIPE, shell=True)
#output, error = process.communicate()

# current image
image = loc.split("/")[-1].split(".")[0]

# params
plane = 0  # to convert all (cut-off, all images planes larger and equal to this value are considered from the image)
tz = 1024  # tile size

# compression methods
comp1 = "LZW"  # "JPEG-2000" #JPEG #"LZW"
comp2 = "jpeg" # "jpeg" #"lzw", "jpeg", "deflate" (zip), "none" # <----- Best to use zip-conversion here(?)
Q2 = 85        # default: 75 (quality of compression)

# output paths (mid-step and final converted and compressed output)
out1 = out_path + image + "_plane_" + str(plane) + "_cm_" + comp1 + ".btf"
out2 = out_path + image + "_test" + "_plane_" + str(plane) + "_cm_" + comp1 +'_' + comp2 + '_Q_' + str(Q2) + ".tif"

# vsi -> btf
sp.check_call(["sh", bfconvert_path, "-tilex", str(tz), "-tiley", str(tz), "-nogroup", "-no-upgrade",
               "-overwrite", "-bigtiff", "-series", str(plane), loc, out1])
# -compression, comp1 <- choose no compression instead in this mid-step

# btf -> tif
sp.check_call(["vips", "tiffsave", out1, out2, "--bigtiff", "--tile", "--pyramid",\
               "--compression=" + comp2, "--Q=" + str(Q2)])

# delete btf file
os.remove(out1)

# kill virtual machine
jb.kill_vm()

t.toc()






