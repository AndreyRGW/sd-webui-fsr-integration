import subprocess
import zipfile
import os
from tempfile import TemporaryDirectory
from PIL import Image
from modules import scripts, modelloader


extension_root = scripts.basedir()
fidelityFX = os.path.join(extension_root, 'FidelityFX-CLI')
fidelityFX_zip = os.path.join(extension_root, 'FidelityFX-CLI.zip')
fidelityFX_exe = os.path.join(fidelityFX, 'FidelityFX_CLI.exe')


def getFidelityFXEXE():
    if not os.path.exists(fidelityFX_exe):
        try:
            # First try with hash_prefix
            modelloader.load_file_from_url(
                url='https://github.com/GPUOpen-Effects/FidelityFX-CLI/releases/download/v1.0.3/FidelityFX-CLI-v1.0.3.zip',
                model_dir=extension_root,
                file_name='FidelityFX-CLI.zip',
                hash_prefix='d280f245730c6d163c0e072a881ed4933b32e67b9de5494650119afa9649ea11',
            )
        except TypeError:
            # If hash_prefix is not supported, try without it
            modelloader.load_file_from_url(
                url='https://github.com/GPUOpen-Effects/FidelityFX-CLI/releases/download/v1.0.3/FidelityFX-CLI-v1.0.3.zip',
                model_dir=extension_root,
                file_name='FidelityFX-CLI.zip'
            )
        with zipfile.ZipFile(fidelityFX_zip, 'r') as zip_ref:
            zip_ref.extractall(fidelityFX)
    return fidelityFX_exe


def runFidelityFX_(scale=None, input_file=None, output_file=None, resize_x=None, resize_y=None):
    exe = getFidelityFXEXE()

    # Command to run FidelityFX
    if resize_x and resize_y:
        cmd = [exe, '-Scale', f'{resize_x}', f'{resize_y}', '-Mode', 'CAS', '-Sharpness', '1.0', input_file, output_file]
    elif scale:
        cmd = [exe, '-Scale', f'{scale}x', f'{scale}x', '-Mode', 'CAS', '-Sharpness', '1.0', input_file, output_file]
    else:
        raise ValueError("Either scale or resize_x and resize_y must be provided")

    if os.name != 'nt':
        cmd = ['wine'] + cmd

    print(' '.join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f'FidelityFX CLI exited with code {result.returncode}. Error: {result.stderr}')


def runFidelityFX(img: Image.Image, scale: int) -> Image.Image:
    tmpInDir = TemporaryDirectory()
    tmpOutDir = TemporaryDirectory()
    try:
        fileIn = os.path.join(tmpInDir.name, 'file.jpg')
        fileOut = os.path.join(tmpOutDir.name, 'file.jpg')
        img.convert('RGB').save(fileIn, quality=100)
        runFidelityFX_(scale, fileIn, fileOut)
        if not os.path.exists(fileOut):
            raise Exception("FidelityFX didn't process any image")
        return Image.open(fileOut)
    finally:
        try:
            tmpInDir.cleanup()
            tmpOutDir.cleanup()
        except:
            pass
