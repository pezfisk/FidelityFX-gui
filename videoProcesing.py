import pathlib
import os
import cv2
import shutil
import procesingBatch


def video2Frames(inputVideo, upscaleFactorEntry, fileCheck):
    print('Extracting frames from video')
    global videoExt
    videoExt = fileCheck
    print("Video extension: " + videoExt)
    global video
    video = inputVideo
    currentDir = str(pathlib.Path("main.py").parent.resolve()) + "\inputBatch"
    print(currentDir)

    try:
        print("Deleting ./inputBatch directory")
        shutil.rmtree(str(pathlib.Path("main.py").parent.resolve()) + "\inputBatch")  
    except OSError:
        print("No directory found")
    else:
        print("Deleted all files in ./inputBatch")
        os.mkdir("inputBatch")
    try:
        print("Deleting outputBatch directory")
        shutil.rmtree(str(pathlib.Path("main.py").parent.resolve()) + "\outputBatch")
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

def frames2video(UwRes, UhRes, upscaleFactor):
    print('yay it worked')
    print(videoExt)
    print(video)
    currentDir = str(pathlib.Path("main.py").parent.resolve()) + "\outputBatch"
    videoFPS = cv2.VideoCapture(video)

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver)  < 3 :
        fps = videoFPS.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = videoFPS.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))


    print(str(os.path.splitext(video)[0]))
    if videoExt == ".gif":
        command = f'ffmpeg.exe -r {fps} -f image2 -i {currentDir}\%08d.png {str(os.path.splitext(video)[0])}_{upscaleFactor}x{videoExt}'
    else:
        command = f'ffmpeg.exe -r {fps} -f image2 -s {UwRes}x{UhRes} -i {currentDir}\%08d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p {str(os.path.splitext(video)[0])}_{upscaleFactor}x{videoExt}'
    print("Command executed: "+ command)
    os.system(command)

    videoFPS.release(); 