import tkinter
import procesingBatch
import procesing

def window():
    # Main GUI config
    window = tkinter.Tk()
    window.title('FidelityFX GUI')
    window.iconbitmap('fsr_logo.ico')
    window.geometry("500x300")
    fidelityLabel = tkinter.Label(window, text= "FidelityFX Image Upscaler").pack()
    photoLabel = tkinter.Label(window, text= "Input file path:").pack()
    inputPhotoEntry = tkinter.Entry(window)
    inputPhotoEntry.pack()
    outputLabel = tkinter.Label(window, text= "Output path: (Don't put anything here for video upscaling!)").pack()
    outputPhotoEntry = tkinter.Entry(window)
    outputPhotoEntry.pack()
    upscaleFactorLabel = tkinter.Label(window, text= "Upscale factor:").pack()
    upscaleFactorEntry = tkinter.Entry(window)
    upscaleFactorEntry.pack()
    upscaleButton = tkinter.Button(window, text= "Upscale!", command= lambda: procesing.upscale(inputPhotoEntry, upscaleFactorEntry, outputPhotoEntry)).pack()


    batchUpscaleFactorLabel = tkinter.Label(window, text= "Batch upscale factor:").pack()
    upscaleFactorBatchEntry = tkinter.Entry(window)
    upscaleFactorBatchEntry.pack()
    batchUpscaleButton = tkinter.Button(window, text= "Upscale!", command= lambda: procesingBatch.batchUpscale(upscaleFactorBatchEntry, inputPhotoEntry)).pack()

    window.mainloop()
