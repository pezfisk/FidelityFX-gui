import os   
import PIL
from PIL import Image
import pathlib
import videoProcesing

def batchUpscale(upscaleFactorBatchEntry, isInputVideo):
    # Procesing
    print("Batch Upscaling")

    currentDir = str(pathlib.Path("main.py").parent.resolve()) + "\inputBatch"
    print(currentDir)

    ext = ['.bmp', '.png', '.ico', '.jpg', '.tif', '.gif']

    print(os.listdir(currentDir))

    for inputPhoto in os.listdir(currentDir):
        if str(os.path.splitext(inputPhoto)[1]) in ext:
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
            command = f"powershell .\FidelityFX_CLI.exe -Scale {UwRes} {UhRes} -Mode {modeSelect} ./inputBatch/{inputPhoto} ./outputBatch/{outputName}.png"
        
            print("Executed command: " + command)
            os.system(command)

            if isInputVideo:
                videoProcesing.frames2video()

        else:
            print("File not found or no more files left.")

# FidelityFX variables
mode = ["EASU", "RCAS", "CAS"]
modeSelect = ""
sharpness = 0