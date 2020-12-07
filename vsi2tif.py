"""
mini change log
added arguments for CLI usage / pass in folder with VSI files now
removed unnecessary modules / changes to base modules where possible
changed from vlibs CLI to python module
fixed JAVA/bftools BF_MAX_MEM env var prob
put code for conversion in 2 functions
PEP 8 ;)
"""
import subprocess as sp
import os
import time
import sys
import pyvips
import argparse
import json

# global config section

input_file_type = 'vsi'
path_to_bfconvert = '../bftools/bfconvert'
java_env_var = {'BF_MAX_MEM': '4g'}
defaults = {
    'compression': 'lzw',
    'plane': 0,
    'tilesize': 1024,
    'quality': 85
}


def vsi_to_bigtiff(path_to_input_file, out_path, bfconvert_bin, compression='LZW', tz=1024, plane=0,
                   java_env=None):
    if java_env is None:
        java_env = {'BF_MAX_MEM': '4g'}
    if os.path.isfile(path_to_input_file):
        input_file_name = os.path.splitext(os.path.split(path_to_input_file)[-1])[0]
    else:
        print('input image: {} not found - aborting'.format(path_to_input_file))
        return None
    path_to_output_file = os.path.join(out_path,
                                       input_file_name + "_plane_" + str(plane) + "_cm_" + compression + ".btf")
    # vsi -> btf
    shell_cmd = ' '.join([bfconvert_bin, "-tilex", str(tz), "-tiley", str(tz), "-nogroup", "-no-upgrade",
                          "-overwrite", "-bigtiff", "-series", str(plane), "-compression", compression.upper(),
                          path_to_input_file, path_to_output_file])
    # capture errors
    try:
        # it's possible to explicitly tell check_call to use a shell and set env vars via env parameter
        sp.check_call(shell_cmd, shell=True, env=java_env)
    except sp.CalledProcessError as error:
        print(error.output)
        return None
    return path_to_output_file


def bigtiff_to_pyramide_tiff(path_to_input_file, out_path, compression='LZW', tz=1024, quality=85):
    if os.path.isfile(path_to_input_file):
        input_file_name = os.path.splitext(os.path.split(path_to_input_file)[-1])[0]
    else:
        print('input image: {} not found - aborting'.format(path_to_input_file))
        return None
    path_to_output_file = os.path.join(out_path,
                                       input_file_name + '_' + compression + '_Q_' + str(
                                           quality) + ".tif")
    # supposedly faster to use the python wrapper for libvips instead of cli tool
    im = pyvips.Image.new_from_file(path_to_input_file)
    # depth doesn't seem to be implemented?
    # depth=pyvips.ForeignDzDepth.ONEPIXEL
    im.write_to_file(path_to_output_file, compression=compression.lower(), Q=quality, pyramid=True, tile=True,
                     tile_width=tz, tile_height=tz,
                     bigtiff=True)
    return path_to_output_file


if __name__ == '__main__':
    # pre start checks
    if not os.path.isfile(path_to_bfconvert):
        print('bfconvert not found in {} - aborting'.format(path_to_bfconvert))
        sys.exit(1)

    parser = argparse.ArgumentParser(description='vsi2tif - easy conversion of VSI files to pyramid bigtiff')
    parser.add_argument("input", help="folder with input files")
    parser.add_argument("output", help="folder for output files")
    parser.add_argument("--compression",
                        help="Compression to use for tiff - default {} - use something that is compatible with "
                             "bfconvert and libvips - no checks implemented yet!".format(defaults['compression']),
                        default=defaults['compression'])
    parser.add_argument("--plane", help="Plane to use from VSI - default {}".format(defaults['plane']),
                        default=defaults['plane'])
    parser.add_argument("--tilesize", help="Tilesize to use during conversion and in final image - default {}".format(
        defaults['tilesize']), default=defaults['tilesize'])
    parser.add_argument("--quality", help="Quality value for (if used by compression) final image - default {}".format(
        defaults['quality']), default=defaults['quality'])
    parser.add_argument("--keep_tmp_files", help="If given files from vsi to bigtiff conversion won't be deleted",
                        action='store_true')
    args = parser.parse_args()
    # use std lib time for timing
    start = time.time()
    # check and make out folder
    if not os.path.exists(args.output):
        os.mkdir(args.output)
    if os.path.exists(args.input):
        input_files = []
        for current_dir, dirs, files in os.walk(args.input):
            for file in files:
                if input_file_type in file:
                    input_files.append(os.path.join(current_dir, file))
                    print('Found img {}'.format(os.path.join(current_dir, file)))
        # start the main proc loop -
        # TODO check if it works to run in parallel batches as multiprocs or multithreads
        results_dict = {}
        for in_file in input_files:
            results_dict[in_file] = {}
            result_vsi2bt = vsi_to_bigtiff(in_file, args.output, path_to_bfconvert, compression=args.compression,
                                           tz=args.tilesize, plane=args.plane, java_env=java_env_var)
            if result_vsi2bt is not None:
                result = bigtiff_to_pyramide_tiff(result_vsi2bt, args.output, compression=args.compression,
                                                  tz=args.tilesize,
                                                  quality=args.quality)
                if result is not None:
                    results_dict[in_file]['final_tiff'] = result
                    results_dict[in_file]['parameters'] = {
                        'compression': args.compression,
                        'plane': args.plane,
                        'tilesize': args.tilesize,
                        'quality': args.quality
                    }
                    print('Successfully converted {} to {}'.format(in_file, result))
                    if not args.keep_tmp_files:
                        os.remove(result_vsi2bt)
                    else:
                        results_dict[in_file]['tmp_btiff'] = result_vsi2bt
                else:
                    print('bigtiff to tiled tiff conversion failed - skipping file: {}'.format(in_file))
                    results_dict[in_file]['final_tiff'] = 'skipped due to error in bigtiff_to_pyramide_tiff()'
            else:
                print('vsi to bigtiff conversion failed - skipping file: {}'.format(in_file))
                results_dict[in_file]['final_tiff'] = 'skipped due to error in vsi_to_bigtiff()'
    else:
        print('Input folder does not exist - aborting')
        sys.exit(1)

    with open(os.path.join(args.output, 'processed_files_info.json'), 'w') as json_file:
        json.dump(results_dict, json_file)

    print('Done - the whole processing of {} files took {} seconds'.format(time.time() - start, len(input_files)))
