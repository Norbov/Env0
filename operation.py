import os
import platform

# line ending
WINDOWS_LINE_ENDING = b"\r\n"
UNIX_LINE_ENDING = b"\n"


def detectLineEndings(filePath):
    with open(filePath, "rb") as f:
        for line in f:
            if line.endswith(b"\r\n"):
                return "CRLF"
            elif line.endswith(b"\n"):
                return "LF"
    return "Unknown"


def detectOs():
    return platform.system()


def repeareLineOfEnd(file_path, new_file_path):
    if platform.system() == "Windows":
        if detectLineEndings(file_path) == "LF":
            with open(new_file_path, "rb") as f:
                filedata = f.read()
            filedata = filedata.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
            with open(new_file_path, "wb") as f:
                f.write(filedata)
    elif platform.system() == "Linux":
        if detectLineEndings(file_path) == "CRLF":
            with open(new_file_path, "rb") as f:
                filedata = f.read()
            filedata = filedata.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)
            with open(new_file_path, "wb") as f:
                f.write(filedata)
