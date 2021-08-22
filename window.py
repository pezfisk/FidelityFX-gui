import tkinter
import procesing
import main

#def procesingPrep():
    #procesing.upscaling()

def window():
    # Main GUI config
    window = tkinter.Tk()
    window.title('FidelityFX GUI')
    window.geometry("900x700")
    fidelityLabel = tkinter.Label(window, text= "FidelityFX Image Upscaler")
    fidelityLabel.pack()
    upscaleButton = tkinter.Button(window, text= "Upscale!", command= main.checkData)
    upscaleButton.pack()

    window.mainloop()