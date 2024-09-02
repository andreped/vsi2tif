import os
import subprocess as sp


def vsi2raw(input_path: str, output_path: str, bfconvert: str, compression: str = "LZW", tz: int = 1024, plane: int = 0, max_mem: int = 32) -> None:
    if not os.path.exists(bfconvert):
        raise FileNotFoundError(f"bfconvert not found at: {bfconvert}")
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found at: {input_path}")
    if not os.path.exists(os.path.dirname(output_path)):
        raise FileNotFoundError(f"Output directory not found at: {os.path.dirname}")
    
    cmd = f"{bfconvert} -tilex {tz} -tiley {tz} -nogroup -no-upgrade -overwrite -bigtiff -series {plane} -compression {compression} {input_path} {output_path}"
    sp.check_call(cmd, shell=True, env={"BF_MAX_MEM": f"{max_mem}g"})


def raw2tiff(input_path: str, output_path: str, compression: str = "jpeg", quality: int = 85) -> None:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found at: {input_path}")
    if not os.path.exists(os.path.dirname(output_path)):    
        raise FileNotFoundError(f"Output directory not found at: {os.path.dirname}")
    
    cmd = f"vips tiffsave {input_path} {output_path} --bigtiff --tile --pyramid --compression={compression} --Q={quality}"
    sp.check_call(cmd, shell=True)
