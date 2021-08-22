import tkinter
import procesing

def window():
    # Main GUI config
    window = tkinter.Tk()
    window.title('FidelityFX GUI')
    window.geometry("500x300")
    fidelityLabel = tkinter.Label(window, text= "FidelityFX Image Upscaler").pack()
    photoLabel = tkinter.Label(window, text= "Input photo path:").pack()
    inputPhotoEntry = tkinter.Entry(window)
    inputPhotoEntry.pack()
    outputLabel = tkinter.Label(window, text= "Output path: ").pack()
    outputPhotoEntry = tkinter.Entry(window)
    outputPhotoEntry.pack()
    upscaleFactorLabel = tkinter.Label(window, text= "Upscale factor:").pack()
    upscaleFactorEntry = tkinter.Entry(window)
    upscaleFactorEntry.pack()
    upscaleButton = tkinter.Button(window, text= "Upscale!", command= lambda: procesing.upscale(inputPhotoEntry, upscaleFactorEntry, outputPhotoEntry)).pack()

    window.mainloop()
