import mainWindow
import os

#try:
print("Deleting ./inputBatch directory")
os.rmdir("./inputBatch")
##except OSError:
print("No directory found")
#else:
print("Deleted all files in ./inputBatch")
os.mkdir("./inputBatch")
#try:
print("Deleting outputBatch directory")
os.rmdir("./outputBatch")
#except OSError:
#print("No directory found")
#else:
print("Deleted all files in ./outputBatch")
os.mkdir("./outputBatch")

# try:
#     print("Check for inputBatch folder")
#     os.listdir("./inputBatch")
# except:
#     print("No inputBatch folder found, so created one")
#     os.mkdir("./inputBatch")
# else:
#     print("inputBatch folder has been found")
# try:
#     print("Check for outputBatch folder")
#     os.listdir("./outputBatch")
# except:
#     print("No outputBatch folder found, so created one")
#     os.mkdir("./outputBatch")
# else:
#     print("outputBatch folder has been found")

mainWindow.window()