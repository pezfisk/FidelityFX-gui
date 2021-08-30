import pathlib
import os
import procesingBatch

def video2Frames(inputVideo, upscaleFactorEntry):
    print('Extracting frames from video')
    currentDir = str(pathlib.Path("main.py").parent.resolve()) + "\inputBatch"
    print(currentDir)
    command = f'ffmpeg.exe -i {inputVideo} "{currentDir}\%08d.png"'
    print("Executed command: " + command)
    os.system(command)

    isInputVideo = True

    procesingBatch.batchUpscale(upscaleFactorEntry, isInputVideo)

def frames2video():
    print('yay it worked')