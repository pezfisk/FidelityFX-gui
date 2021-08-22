import tkinter
import procesing

def procesingPrep():
    inputPhoto = inputphotoLabel.get()
    
    upscaleFactor = upscaleFactorLabel.get()
     
    outputPath = outputLabel.get()

    return inputPhoto, upscaleFactor, outputPath

def window():
    # Main GUI config
    window = tkinter.Tk()
    window.title('FidelityFX GUI')
    window.geometry("900x700")
    fidelityLabel = tkinter.Label(window, text= "FidelityFX Image Upscaler")
    fidelityLabel.pack()
    photoLabel = tkinter.Label(window, text= "Input photo path:")
    photoLabel.pack()
    inputPhotoEntry = tkinter.Entry(window)
    inputPhotoEntry.pack()
    outputLabel = tkinter.Label(window, text= "Output path: ")
    outputLabel.pack()
    outputPhotoEntry = tkinter.Entry(window)
    outputPhotoEntry.pack()
    upscaleFactorLabel = tkinter.Label(window, text= "Upscale factor:")
    upscaleFactorLabel.pack()
    upscaleFactorEntry = tkinter.Entry(window)
    upscaleFactorEntry.pack()
    upscaleButton = tkinter.Button(window, text= "Upscale!", command= procesing.checkData)
    upscaleButton.pack()


    window.mainloop()