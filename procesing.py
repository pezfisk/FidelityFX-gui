import os
import PIL
import mainWindow

def upscale():
    # Procesing

    inputPhoto, upscaleFactor, outputPath = mainWindow.procesingPrep

    image_file = inputPhoto
    img = PIL.Image.open(image_file)
    wRes, hRes = img.size

    print("wRes: " + str(wRes) + " hRes: " + str(hRes))
    modeSelect = mode[0]
    os.system(f'FidelityFX_CLI.exe -Scale {wRes * upscaleFactor} {hRes * upscaleFactor} -Mode {modeSelect} {inputPhoto} {outputPath}')

def checkData():
    #upscaleFactor = 2
    #if upscaleFactor < 1:
        #upscaleFactor = 1
    #else:
    upscale()

# FidelityFX variables
mode = ["EASU", "RCAS", "CAS"]
modeSelect = ""
sharpness = 0