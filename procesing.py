import os   
import PIL
from PIL import Image
import videoProcesing
import mainWindow

def upscale(inputPhoto, upscaleFactorEntry): # Output path removed
    # Procesing
    print("Single file upscaling")
    
    print(f'Input photo: {inputPhoto}')

    # print(f'Output Path: {outputPath}')

    upscaleFactor = upscaleFactorEntry.get()
     
    print(f'Upscale factor: {upscaleFactor}')

    videoExt = ['.mp4', '.mov', '.mkv', '.av1', '.avi']
    imageExt = ['.bmp', '.png', '.ico', '.jpg', '.tif', '.gif', '.jpeg', '.jfif']

    fileCheck = os.path.splitext(inputPhoto)[1]
    print(fileCheck)
    if fileCheck in imageExt:
        print('Input file is an image')
        image_file = inputPhoto
        img = PIL.Image.open(image_file)
        wRes, hRes = img.size

        UwRes = int(wRes) * int(upscaleFactor)
        UhRes = int(hRes) * int(upscaleFactor)

        print(f"wRes: {str(wRes)} hRes: {str(hRes)}")
        print(f"Upscaled wRes: {UwRes} UhRes: {UhRes}")
        modeSelect = mode[0]
        outputPath = str(os.path.splitext(inputPhoto)[0]) + "_" + upscaleFactor + "x" + str(os.path.splitext(inputPhoto)[1])
        command = f'powershell ./FidelityFX_CLI.exe -Scale {UwRes} {UhRes} -Mode {modeSelect} {inputPhoto} {outputPath}'
        print("Command executed: ", command)
        os.system(command)  
        #mainWindow.show_image(outputPath)

    else:
        if fileCheck in videoExt:
            print('Input file is a video')
            videoProcesing.video2Frames(inputPhoto, upscaleFactorEntry)
        else:
            print('No more files')

# FidelityFX variables
mode = ["EASU", "RCAS", "CAS"]
modeSelect = ""
sharpness = 0