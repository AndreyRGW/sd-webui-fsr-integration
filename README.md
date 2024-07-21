# AMD FidelityFX Super Resolution (FSR) 1.0 integration

This extension integrates [AMD FidelityFX Super Resolution (FSR) 1.0](https://gpuopen.com/fidelityfx-superresolution/) upscaling feature into [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui). You can use it inside *hires fix*, *upscaler_for_img2img* or in the *extras* tab. You need to have the FidelityFX CLI executable and provide a path to `FidelityFX_CLI.exe` in `Settings/Upscaling` of webui. You can get FidelityFX_CLI from [here](https://github.com/GPUOpen-Effects/FidelityFX-CLI/releases).

![](/images/preview.png)
![](/images/upscalers.png)

To set up the path in Windows, right-click on the `FidelityFX_CLI.exe` file while holding the "Shift" key, and select "Copy as path".

If you're using Linux, you may need to use Wine(?)

This extension offers FSR 1.0 Contrast Adaptive Sharpening upscaling at 2x, 3x, and 4x scales.

Please note that while this integration allows you to use FSR 1.0 within the stable-diffusion-webui environment, there are also other high-quality upscaling options available. Special thanks to light-and-ray, it was his extension with Topaz Photo AI integration as an upscaler for stable diffusion that inspired me to do the AMD FSR integration, so I suggest you check it out [Topaz Photo AI integration](https://github.com/light-and-ray/sd-webui-topaz-photo-ai-integration).

![](/images/comparation.jpg)

If you encounter any issues or have suggestions for improvement, please feel free to open an issue.
