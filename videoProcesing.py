import pathlib
import os
import procesingBatch

def video2Frames(inputVideo, upscaleFactorEntry):
    print('yay it worked')
    currentDir = str(pathlib.Path("main.py").parent.resolve()) + "\inputBatch"
    print(currentDir)
    command = f'ffmpeg -i {inputVideo} "{currentDir}\%08d.png"'
    print(command)
    os.system(command)

    procesingBatch.batchUpscale(upscaleFactorEntry)