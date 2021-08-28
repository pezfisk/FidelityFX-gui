import os   
import PIL
from PIL import Image
import pathlib

def batchUpscale(upscaleFactorBatchEntry):
    # Procesing
    print("Batch Upscaling")

    currentDir = str(pathlib.Path("main.py").parent.resolve()) + "\inputBatch"
    print(currentDir)

    for inputPhoto in os.listdir(currentDir):
        print(inputPhoto)

        upscaleFactor = upscaleFactorBatchEntry.get()
            
        print(f'Upscale factor: {upscaleFactor}')

        img = PIL.Image.open(currentDir + "/" + inputPhoto)
        wRes, hRes = img.size

        UwRes = int(wRes) * int(upscaleFactor)
        UhRes = int(hRes) * int(upscaleFactor)

        print(f"wRes: {str(wRes)} hRes: {str(hRes)}")
        print(f"Upscaled wRes: {UwRes} UhRes: {UhRes}")

        outputName = os.path.splitext(inputPhoto)[0]

        modeSelect = mode[0]
        command = f"powershell ./FidelityFX_CLI.exe -Scale {UwRes} {UhRes} -Mode {modeSelect} ./inputBatch/{inputPhoto} ./outputBatch/{outputName}.png"
    
        print("Executed command: " + command)
        os.system(command)

    else:
        print("File not found")


# FidelityFX variables
mode = ["EASU", "RCAS", "CAS"]
modeSelect = ""
sharpness = 0