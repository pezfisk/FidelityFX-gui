import os
import PIL
from main import *

def upscale():
    # Procesing
    image_file = inputPhoto
    img = PIL.Image.open(image_file)
    wRes, hRes = img.size

    print("wRes: " + str(wRes) + " hRes: " + str(hRes))
    modeSelect = mode[0]
    os.system(f'FidelityFX_CLI.exe -Scale {wRes * upscaleFactor} {hRes * upscaleFactor} -Mode {modeSelect} {inputPhoto} {outputPath}')

# FidelityFX variables
mode = ["EASU", "RCAS", "CAS"]
modeSelect = ""
sharpness = 0