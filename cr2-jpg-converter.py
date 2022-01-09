import rawpy
import imageio
import os
import tkinter as tk
from tkinter import filedialog

class ImageConverter:
    def __init__(self):
        window = tk.Tk()
        window.title("CR2 to JPG Converter")
        window.geometry("600x400")

        self.inputFolderPath = tk.StringVar()
        self.outputFolderPath = tk.StringVar()
        self.status = tk.StringVar()

        inputFolderLabelControl = tk.Label(window, text = "Input Folder").grid(row = 0, column = 0)
        inputFoldercontrol = tk.Button(window, text="Browse", command=self.browseInputFolder).grid(row = 0, column = 1)
        inputFolderValueLabelControl = tk.Label(window, textvariable = self.inputFolderPath).grid(row = 0, column = 2)

        outputFolderLabelControl = tk.Label(window, text = "Output Folder").grid(row = 1, column = 0)
        outputFoldercontrol = tk.Button(window, text="Browse", command=self.browseOutputFolder).grid(row = 1, column = 1)
        outputFolderValueLabelControl = tk.Label(window, textvariable = self.outputFolderPath).grid(row = 1, column = 2)

        statusLabelControl = tk.Label(window, textvariable = self.status, fg='#00f').grid(row = 3, column = 0, columnspan=2)

        submitButtonControl = tk.Button(window, text = "Submit", command=self.processImages).grid(row = 4, column = 0, columnspan=2)

        window.mainloop()

    def processImages(self):
        if(self.isInValid()):
            self.status.set('Input & Output folder is mandatory')
            return

        self.status.set('Processing...')
        inputFolder = os.fsencode(self.inputFolderPath.get())

        for rawImage in os.listdir(inputFolder):
            rawImageFilename = os.fsdecode(rawImage)
            rawFilePath = self.inputFolderPath.get() + '\\' + rawImageFilename
            
            if rawImageFilename.endswith(('.CR2')):
                rawFile = rawpy.imread(rawFilePath)
                processedData = rawFile.postprocess()
                outputFilePath = self.outputFolderPath.get() + '\\' + rawImageFilename[:-4] +'.jpg'
                imageio.imsave(outputFilePath, processedData)

        self.status.set('Process Completed !')

    def isInValid(self):
        return (not(self.inputFolderPath.get() and self.inputFolderPath.get().strip()) or not(self.outputFolderPath.get() and self.outputFolderPath.get().strip()))

    def browseInputFolder(self):
        self.status.set('')
        self.inputFolderPath.set(filedialog.askdirectory())

    def browseOutputFolder(self):
        self.status.set('')
        self.outputFolderPath.set(filedialog.askdirectory())

ImageConverter()