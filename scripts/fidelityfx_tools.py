import subprocess, os
from tempfile import TemporaryDirectory
from PIL import Image
import gradio as gr
from modules import shared, script_callbacks

def on_ui_settings():
    shared.opts.add_option(
        "fidelityfx_cli_exe",
        shared.OptionInfo(
            "",
            "Path to FidelityFX CLI executable: FidelityFX_CLI.exe",
            gr.Textbox,
            section=('upscaling', "Upscaling")
        )
    )

script_callbacks.on_ui_settings(on_ui_settings)

def getFidelityFXEXE():
    exe = shared.opts.data.get("fidelityfx_cli_exe", "")
    if not exe or not os.path.exists(exe):
        raise Exception(f'FidelityFX CLI executable file is not found. Please set it up in Settings/Upscaling')
    return exe

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
