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
        modelloader.load_file_from_url(
            url='https://github.com/GPUOpen-Effects/FidelityFX-CLI/releases/download/v1.0.3/FidelityFX-CLI-v1.0.3.zip',
            model_dir=extension_root,
            file_name='FidelityFX-CLI.zip',
            hash_prefix='d280f245730c6d163c0e072a881ed4933b32e67b9de5494650119afa9649ea11',
        )
        with zipfile.ZipFile(fidelityFX_zip, 'r') as zip_ref:
            zip_ref.extractall(fidelityFX)
    return fidelityFX_exe


def runFidelityFX_(scale, input_file, output_file):
    exe = getFidelityFXEXE()
    cmd = [exe, '-Scale', f'{scale}x', f'{scale}x', '-Mode', 'CAS', '-Sharpness', '1.0', input_file, output_file]
    print(' '.join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f'FidelityFX CLI exited with code {result.returncode}. Error: {result.stderr}')


def runFidelityFX(img: Image.Image, scale: int) -> Image.Image:
    tmpInDir = TemporaryDirectory()
    tmpOutDir = TemporaryDirectory()
    try:
        fileIn = os.path.join(tmpInDir.name, 'file.png')
        fileOut = os.path.join(tmpOutDir.name, 'file.png')
        img.convert('RGB').save(fileIn, 'PNG')
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
