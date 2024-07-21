from dataclasses import dataclass
from modules.upscaler import Upscaler, UpscalerData
from scripts.fidelityfx_tools import runFidelityFX

@dataclass
class Fields:
    scale: int

data = [
    Fields(2),
    Fields(3),
    Fields(4),
]

class BaseClass(Upscaler):
    def __init__(self, dirname, fields: Fields = None):
        if fields is None:
            self.scalers = []
            return
        self.name = "FidelityFX"
        self.fields = fields
        self.scalers = [UpscalerData(f'FidelityFX Super Resolution {self.fields.scale}x', None, self, self.fields.scale)]
        super().__init__()

    def do_upscale(self, img, selected_model):
        return runFidelityFX(img, self.fields.scale)

class Class0(BaseClass, Upscaler):
    def __init__(self, dirname):
        super().__init__(dirname, data[0])

class Class1(BaseClass, Upscaler):
    def __init__(self, dirname):
        super().__init__(dirname, data[1])

class Class2(BaseClass, Upscaler):
    def __init__(self, dirname):
        super().__init__(dirname, data[2])