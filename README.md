# AMD FidelityFX Super Resolution (FSR) 1.0 integration

This extension integrates [AMD FidelityFX Super Resolution (FSR) 1.0](https://gpuopen.com/fidelityfx-superresolution/) upscaling feature into [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui). AMD FSR1 is based on Lanczos upscale, so don't expect anything amazing. You can use it inside *hires fix*, *upscaler_for_img2img* or in the *extras* tab. 

Extension will automatically download the FidelityFX_CLI executable during the first run. No manual setup is required. For linux you need to have `wine` in `PATH`

![](/images/preview.png)
![](/images/upscalers.png)

This extension offers FSR 1.0 Contrast Adaptive Sharpening upscaling at 2x, 3x, and 4x scales, as well as in a universal mode that is tied to the scale you set in hiresfix.

# Platform Support
This extension is primarily designed for Windows. For linux you need to have `wine` in `PATH`

# Notes
Please note that while this integration allows you to use FSR 1.0 within the stable-diffusion-webui environment, there are also other high-quality upscaling options available. Special thanks to light-and-ray, it was his extension with Topaz Photo AI integration as an upscaler for stable diffusion that inspired me to do the AMD FSR integration, so I suggest you check it out [Topaz Photo AI integration](https://github.com/light-and-ray/sd-webui-topaz-photo-ai-integration).

![](/images/comparation.jpg)

If you encounter any issues or have suggestions for improvement, please feel free to open an issue.
