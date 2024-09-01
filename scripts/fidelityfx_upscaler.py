from dataclasses import dataclass
from modules.upscaler import Upscaler, UpscalerData
from modules.processing import StableDiffusionProcessingTxt2Img
from modules.processing import Processed
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
        # Check which parameters to use
        if hasattr(self.fields, 'resize_x') and hasattr(self.fields, 'resize_y'):
            return runFidelityFX(img=img, scale=None, resize_x=self.fields.resize_x, resize_y=self.fields.resize_y)
        else:
            return runFidelityFX(img=img, scale=self.fields.scale)
        
class FidelityFXUniversal(Upscaler):
    def __init__(self, dirname):
        self.name = "FidelityFX Universal"
        self.scalers = [UpscalerData('FidelityFX Universal', None, self, None)]
        super().__init__()

    def upscale(self, img, scale, data_path=None, selected_model=None):
        p = getattr(self, 'processing', None)
        
        if isinstance(p, StableDiffusionProcessingTxt2Img):
            if p.hr_resize_x and p.hr_resize_y:
                return runFidelityFX(img, scale=None, resize_x=p.hr_resize_x, resize_y=p.hr_resize_y)
            elif p.hr_scale:
                return runFidelityFX(img, scale=p.hr_scale)
        
        # If p does not exist or does not contain the necessary parameters, use the passed scale
        if scale:
            return runFidelityFX(img, scale=scale)
        
        # If none of the options are suitable, use the original image
        return img

class Class0(BaseClass, Upscaler):
    def __init__(self, dirname):
        super().__init__(dirname, data[0])

class Class1(BaseClass, Upscaler):
    def __init__(self, dirname):
        super().__init__(dirname, data[1])

class Class2(BaseClass, Upscaler):
    def __init__(self, dirname):
        super().__init__(dirname, data[2])