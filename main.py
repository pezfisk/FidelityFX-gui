import tkinter
import PIL
from PIL import Image
import os
import pathlib
window = tkinter.Tk()
window.title('FidelityFX GUI')

mode = ["EASU", "RCAS", "CAS"]
modeSelect = ""
sharpness = 0

inputPhoto = input("Input photo: ")
outputPath = input("Output photo: ")
upscaleFactor = int(input("Upscale factor: "))

image_file = inputPhoto
img = PIL.Image.open(image_file)
wRes, hRes = img.size

print("wRes: " + str(wRes) + " hRes: " + str(hRes))
modeSelect = mode[0]
os.system(f'FidelityFX_CLI.exe -Scale {wRes * upscaleFactor} {hRes * upscaleFactor} -Mode {modeSelect} {inputPhoto} {outputPath}')