import os   
import PIL
from PIL import Image
import videoProcesing

def upscale(inputPhotoEntry, upscaleFactorEntry, outputPhotoEntry):
    # Procesing
    print("Single file upscaling")

    inputPhoto = inputPhotoEntry.get()
    
    print(f'Input photo: {inputPhoto}')

    outputPath = outputPhotoEntry.get()

    print(f'Output Path: {outputPath}')

    upscaleFactor = upscaleFactorEntry.get()
     
    print(f'Upscale factor: {upscaleFactor}')

    videoExt = ['.mp4', '.mov', '.mkv', '.av1', '.avi']
    imageExt = ['BMP', 'PNG', 'ICO', 'JPG', 'TIF', 'GIF']

    fileCheck = os.path.splitext(inputPhoto)[1]
    print(fileCheck)
    if str(imageExt) in fileCheck:
        print('Input file is an image')
        image_file = inputPhoto
        img = PIL.Image.open(image_file)
        wRes, hRes = img.size

        UwRes = int(wRes) * int(upscaleFactor)
        UhRes = int(hRes) * int(upscaleFactor)

        print(f"wRes: {str(wRes)} hRes: {str(hRes)}")
        print(f"Upscaled wRes: {UwRes} UhRes: {UhRes}")
        modeSelect = mode[0]
        os.system(f'powershell ./FidelityFX_CLI.exe -Scale {UwRes} {UhRes} -Mode {modeSelect} {inputPhoto} {outputPath}')
    else:
        if fileCheck in str(fileCheck):
            print('Input file is a video')
            videoProcesing.video2Frames(inputPhoto, upscaleFactorEntry)
        else:
            print('No more files')

# FidelityFX variables
mode = ["EASU", "RCAS", "CAS"]
modeSelect = ""
sharpness = 0