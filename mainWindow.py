import tkinter
from tkinter import filedialog
import procesingBatch
import procesing
import cv2

def show_image(inputPhoto):
    #img = cv2.imread(inputPhoto, cv2.IMREAD_COLOR)
    #cv2.imshow("uwu", img)
    return True

def getImageInput():
    global inputDialog
    inputDialog = filedialog.askopenfilename(title="Select input file", filetypes=(("All files", "*.*"), ("png files", "*.png"),("jpg files", "*.jpg"), ("ico files","*.ico"), ("tif files", "*.tif"), ("gif files", "*.gif"), ("mp4 files", "*.mp4"), ("mov files","*.mov"), ("mkv files","*.mkv"), ("av1 files","*.av1"), ("avi files", "*.avi")))

def getImageOutputDir():
    global outputDialog
    outputDialog = filedialog.askdirectory(title="Select output path")


def window():
    # Main GUI config
    window = tkinter.Tk()
    window.title('FidelityFX GUI')
    window.iconbitmap('fsr_logo.ico')
    window.geometry("500x300")
    fidelityLabel = tkinter.Label(window, text= "FidelityFX Image Upscaler").pack()
    photoButton = tkinter.Button(window, text="Select file", command=getImageInput).pack()
    #outputButton = tkinter.Button(window, text= "Output path: (Don't put anything here for video upscaling!)", command=getImageOutputDir).pack()
    upscaleFactorLabel = tkinter.Label(window, text= "Upscale factor:").pack()
    upscaleFactorEntry = tkinter.Entry(window)
    upscaleFactorEntry.pack()
    upscaleButton = tkinter.Button(window, text= "Upscale!", command= lambda: procesing.upscale(inputDialog, upscaleFactorEntry)).pack()

    batchUpscaleFactorLabel = tkinter.Label(window, text= "Batch upscale factor:").pack()
    upscaleFactorBatchEntry = tkinter.Entry(window)
    upscaleFactorBatchEntry.pack()
    batchUpscaleButton = tkinter.Button(window, text= "Upscale!", command= lambda: procesingBatch.batchUpscale(upscaleFactorBatchEntry, inputPhotoEntry)).pack()

    window.mainloop()
