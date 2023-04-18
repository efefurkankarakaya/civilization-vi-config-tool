import os
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET

from fontHandler import readFontXML, updateFontXML, saveChangesToXML
from optionHandler import readOptionsFile, updateOption, saveOptions

FONT_MULTIPLIER = 1.3
SCALE_RATE = 0.25

ALIAS = 'Civilization VI Config Tool'

HOME = str(Path.home())
FONTS = os.path.join(HOME, "Library/Application Support/Steam/steamapps/common/Sid Meier's Civilization VI/Civ6.app/Contents/Assets/Base/Assets/UI/Fonts")
OPTIONS = os.path.join(HOME, "Library/Application Support/Sid Meier's Civilization VI")
FONTS_FILENAME = "Civ6_FontStyles_EFIGS_bak.xml"
OPTIONS_FILENAME = "AppOptions.txt"
BACKUP = "backup"

def createFolder(path):
    fullPath = os.path.join(path, 'backup')
    try:
        if not os.path.exists(fullPath):
            os.mkdir(fullPath)
    except Exception as error:
        print(error)

def copyFile(source, destination):
    if not os.path.exists(destination):
        shutil.copy(source, destination)

def makeBackup():
    source = os.path.join(FONTS, FONTS_FILENAME)
    destination = os.path.join(FONTS, BACKUP, FONTS_FILENAME)
    copyFile(source, destination)

    source = os.path.join(OPTIONS, OPTIONS_FILENAME)
    destination = os.path.join(OPTIONS, BACKUP, OPTIONS_FILENAME)
    copyFile(source, destination)

def updateFont(multiplier):
    if not multiplier:
        multiplier = 1

    try:
        source = os.path.join(FONTS, FONTS_FILENAME)
        destination = source
        content = readFontXML(source)
        tree = updateFontXML(content, sizeMultiplier=multiplier)
        saveChangesToXML(tree, destination)
        print(f"Updated font size by multiplying {multiplier}")
    except Exception as exception:
        print(exception)

def updateUIUpscaling(rate):
    if not rate:
        rate = "0.25"

    try:
        destination = os.path.join(OPTIONS, OPTIONS_FILENAME)
        source = destination
        content = readOptionsFile(source)
        updatedOne = updateOption(content, "UIUpscale", rate)
        saveOptions(content, destination)
        print(updatedOne)
    except Exception as exception:
        print(exception)

try:
    createFolder(FONTS)
    createFolder(OPTIONS)
    makeBackup()
    # updateFont(1.3)
    updateUIUpscaling(SCALE_RATE)
except Exception as exception:
    print(exception) 

