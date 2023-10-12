# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import ttk
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *
import os

import cv2

from matplotlib import pyplot as plt, gridspec
import numpy as np
import csv

from pathlib import Path
from matplotlib.pyplot import subplots_adjust


fileName = ""
initialDir = ""


def imadjustAuto(x):
    # Similar to imadjust in MATLAB.
    # Converts an image range from [a,b] to [c,d].
    # The Equation of a line can be used for this transformation:
    #   y=((d-c)/(b-a))*(x-a)+c
    # However, it is better to use a more generalized equation:
    #   y=((x-a)/(b-a))^gamma*(d-c)+c
    # If gamma is equal to 1, then the line equation is used.
    # When gamma is not equal to 1, then the transformation is not linear.
    gamma = 1.0
    a = np.min(x)
    b = np.max(x)
    c = 0.0
    d = 255.0

    y = (((x - a) / (b - a)) ** gamma) * (d - c) + c
    # y = (cv2.divide((cv2.subtract(x,a)),(cv2.subtract(b,a)),dtype=np.uint8) ** gamma) * (d - c) + c
    return y

def imadjustManual(x, MIN, MAX):
    # Similar to imadjust in MATLAB.
    # Converts an image range from [a,b] to [c,d].
    # The Equation of a line can be used for this transformation:
    #   y=((d-c)/(b-a))*(x-a)+c
    # However, it is better to use a more generalized equation:
    #   y=((x-a)/(b-a))^gamma*(d-c)+c
    # If gamma is equal to 1, then the line equation is used.
    # When gamma is not equal to 1, then the transformation is not linear.
    gamma = 1.0
    a = np.min(x)
    b = np.max(x)
    c = 0.0
    d = 255.0

    y = (((x - MIN) / (MAX - MIN)) ** gamma) * (d - c) + c
    # y = (cv2.divide((cv2.subtract(x,a)),(cv2.subtract(b,a)),dtype=np.uint8) ** gamma) * (d - c) + c
    return y


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def selectDir():
    global initialDir, path
    text2.delete(1.0, END)
    text1.delete(1.0, END)
    initialDir = askdirectory(parent=window)
    text1.insert(INSERT, initialDir)
    path = Path(initialDir)
    text2.insert(INSERT, path)



def Adjust():
    global fileName, initialDir, path
    # files = [path.name for path in Path(initialDir).glob('*BW*.jpg')]
    # files = list(path.glob('*BW*.jpg'))

    for root, dirs, files in os.walk(initialDir):
        for file in files:
            if (file.endswith("BW.jpg")):
                fileName = os.path.join(root, file)
                print(fileName)
                im = cv2.imread(fileName)
                im = imadjustAuto(im)
                cv2.imwrite(fileName, im)
    # print(files)
    text2.delete(1.0, END)
    text2.insert(INSERT, "Ready!")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('1350x250')
    window.title("BW_MASS_ADJUSTER")

    text1 = Text(width=70, height=1)  # image
    text1.grid(column=1, row=0, sticky=W)
    text2 = Text(width=70, height=1)  # Background
    text2.grid(column=1, row=1, sticky=W)

    btn1 = Button(window, text="Select Dir", command=selectDir)
    btn1.grid(column=0, row=0, sticky=W)
    btn2 = Button(window, text="ADJUST", command=Adjust)
    btn2.grid(column=0, row=1, sticky=W)

    window.mainloop()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/