import sys
import os
import comtypes
import comtypes.client
from pyfiglet import Figlet
from ppt2pdf.utils import generateOutputFilename
from comtypes.client import CreateObject, Constants



def convert(inputFilePath,outputFilePath):

    # print("Your Input file is at:")
    # print(inputFilePath)
    if(not outputFilePath):
        outputFilePath = generateOutputFilename(inputFilePath);
    
    # print("Your Output file will be at:")
    # print(outputFilePath);
    # %% Create powerpoint application object
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    #%% Set visibility to minimize
    powerpoint.Visible = 1
    #%% Open the powerpoint slides
    slides = powerpoint.Presentations.Open(inputFilePath)
    #%% Save as PDF (formatType = 32)
    slides.SaveAs(outputFilePath, 32)
    #%% Close the slide deck
    slides.Close()


convert(os.path.dirname(__file__)+'\\input\\'+'examples.pptx',os.path.dirname(__file__)+'\\pdf\\'+'presentation.pdf')
