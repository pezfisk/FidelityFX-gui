import pathlib
import os
import cv2
import procesingBatch


def video2Frames(inputVideo, upscaleFactorEntry):
    print('Extracting frames from video')
    currentDir = str(pathlib.Path("main.py").parent.resolve()) + "\inputBatch"
    print(currentDir)

    try:
        print("Deleting ./inputBatch directory")
        os.rmdir("./inputBatch")
    except OSError:
        print("No directory found")
    else:
        print("Deleted all files in ./inputBatch")
        os.mkdir("./inputBatch")
    try:
        print("Deleting outputBatch directory")
        os.rmdir("./outputBatch")
    except OSError:
        print("No directory found")
    else:
        print("Deleted all files in ./outputBatch")
        os.mkdir("./outputBatch")

    command = f'ffmpeg.exe -i {inputVideo} "{currentDir}\%08d.png"'
    print("Executed command: " + command)
    os.system(command)

    isInputVideo = True 

    procesingBatch.batchUpscale(upscaleFactorEntry, isInputVideo)

def frames2video(inputVideo):
    print('yay it worked')
    video = cv2.VideoCapture(inputVideo)
    videoFps = video.get(cv2.CAP_PROP_FPS)
    print(videoFps)