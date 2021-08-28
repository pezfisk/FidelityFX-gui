import os   
import PIL
from PIL import Image

def upscale(inputPhotoEntry, upscaleFactorEntry, outputPhotoEntry):
    # Procesing
    inputPhoto = inputPhotoEntry.get()
    
    print(f'Input photo: {inputPhoto}')

    outputPath = outputPhotoEntry.get()

    print(f'Output Path: {outputPath}')

    upscaleFactor = upscaleFactorEntry.get()
     
    print(f'Upscale factor: {upscaleFactor}')

    image_file = inputPhoto
    img = PIL.Image.open(image_file)
    wRes, hRes = img.size

    UwRes = int(wRes) * int(upscaleFactor)
    UhRes = int(hRes) * int(upscaleFactor)

    print(f"wRes: {str(wRes)} hRes: {str(hRes)}")
    print(f"Upscaled wRes: {UwRes} UhRes: {UhRes}")
    modeSelect = mode[0]
    os.system(f'powershell ./FidelityFX_CLI.exe -Scale {UwRes} {UhRes} -Mode {modeSelect} {inputPhoto} {outputPath}')

# FidelityFX variables
mode = ["EASU", "RCAS", "CAS"]
modeSelect = ""
sharpness = 0