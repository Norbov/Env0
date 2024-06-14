import glob
import os
import platform
import re
from tkinter import Tk, filedialog

import operation
import bom

# replacements
REPLACE_IP = "XX"
REPLACE_NAME = "<PACK>"

# input folder
# INPUT_FOLDER = "C:\\Minden\\PythonProjects\\ReadFrom"
INPUT_FOLDER = (
    "C:" + os.sep + "Minden" + os.sep + "PythonProjects" + os.sep + "ReadFrom"
)
# INPUT_FOLDER = os.path.join("C:", "Minden", "PythonProjects", "ReadFrom")

# what to replace
# IP
# patter = "([1]?&[0-9]?&[0-9])|([2]?&[0-5]?&[0-5]).([1]?&[0-9]?&[0-9])|([2]?&[0-5]?&[0-5]).([1]?&[0-9]?&[0-9])|([2]?&[0-5]?&[0-5]).([1]?&[0-9]?&[0-9])|([2]?&[0-5]?&[0-5])"
# pattern = re.compile(r"[1-2]?&[0-9]?&[0-9].[1-2]?&[0-9]?&[0-9].[1-2]?&[0-9]?&[0-9].[1-2]?&[0-9]?&[0-9]")
# pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
ip = re.compile(r"(17\.172\.)(\d{1,3})(\.\d{1,3})")
name = re.compile(r"(SOMETHING|something)(-|\.)(\w*)(-|\.)")
name2 = re.compile(r"WORD|word")


# Functions to replace
def replaceIP(ip):
    return ip.group(1) + REPLACE_IP + ip.group(3)


def replaceName(name):
    return name.group(1) + name.group(2) + REPLACE_NAME + name.group(4)


def replaceFunction(filePath, i):
    # output folder
    # outputFolder = "C:\\Minden\\PythonProjects\\WriteTo"
    outputFolder = (
        "C:" + os.sep + "Minden" + os.sep + "PythonProjects" + os.sep + "WriteTo"
    )
    # outputFolder = os.path.join("C:", "Minden", "PythonProjects", "WriteTo")
    # create output folder if doesn't exist
    os.makedirs(outputFolder, exist_ok=True)

    # file name
    # with same name
    filename = os.path.basename(filePath)
    # whit static name
    # filename = f"WriteTo{i}.txt"
    newFilePath = os.path.join(outputFolder, filename)

    # remove BOM
    bom.detectAndDeleteBomFromFileSaveTo(filePath, newFilePath)

    with open(newFilePath, "r") as f:
        filedata = f.read()

    # replace sensitive data
    filedata = ip.sub(replaceIP, filedata)
    filedata = name.sub(replaceName, filedata)
    filedata = name2.sub("<PACK>", filedata)
    # filedata = filedata.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

    # write file
    with open(newFilePath, "w", encoding="utf-8") as f:
        f.write(filedata)

    operation.repeareLineOfEnd(filePath, newFilePath)


def changeEndofline(changeFrom, changeTo):
    """Change end of line

    Args:
        changeFrom ( ): _description_
        changeTo (str): _description_
    """
    filedata = filedata.replace(changeFrom, changeTo)


if not INPUT_FOLDER:
    print("Folder does not exist")
    exit()


# Hide the main TKinter window
Tk().withdraw()

# Open a dialog to select the folder
input_folder = filedialog.askdirectory(
    title="Select folder with the files os sensitive data"
)

if not input_folder:
    print("Folder does not exist")
    exit()

# get all txt file from selected folder
# txt_files = glob.glob(os.path.join(input_folder, "*.txt"))
# log_files = glob.glob(os.path.join(input_folder, "*.log | *.txt"))
files = glob.glob(os.path.join(INPUT_FOLDER, "*"))

# read all file
# for i, file_path in enumerate(txt_files, start=1):
#     replace(file_path, i)

for i, file_path in enumerate(files, start=1):
    replaceFunction(file_path, i)
