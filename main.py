import mainWindow
import os

try:
    print("Check for inputBatch folder")
    os.listdir("./inputBatch")
except:
    print("No inputBatch folder found, so created one")
    os.mkdir("./inputBatch")
else:
    print("inputBatch folder has been found")
try:
    print("Check for outputBatch folder")
    os.listdir("./outputBatch")
except:
    print("No outputBatch folder found, so created one")
    os.mkdir("./outputBatch")
else:
    print("outputBatch folder has been found")

mainWindow.window()