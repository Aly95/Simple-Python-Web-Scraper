import urllib.request as url
import re
import webbrowser

imageTypeList = [".jpg", ".png"]
imageTagList = ["href=", "src="]

# Retrieves and returns the data from the URL using the urllib module
def getDataFromUrl(myUrl: str):
    res = url.urlopen(myUrl)
    data = res.readlines()
    return data

# Searches the data for an image, and returns the line if found
def getImageList(data: str):
    imageList = []
    for line in data:
        if checkForImageTags(line):
            if checkForImageFormats(line):
                imageList.append(line)
    return imageList

def checkForImageTags(line: str):
    tagCheck = False
    for tag in imageTagList:
        if(tag.encode() in line):
            tagCheck = True
    return tagCheck

def checkForImageFormats(line: str):
    for type in imageTypeList:
        if(type.encode() in line):
            return True
        else:
            return False

# Retrieves a list of all data within quotation marks
def getUrlFromImgLine(line: str):
    dataWithinQuotationMarks = re.findall(r'"(.*?)(?<!\\)"', line) # Creates a list of strings of lines between quotation marks
    for x in dataWithinQuotationMarks:
        for type in imageTypeList:
            if(type in x):
                return x

# Opens the given URL using the webbrowser module
def openWebsite(url: str):
    webbrowser.open(url)

# Searches the data for an image, and returns the line if found
def getImagePathsClone(data: str):
    imageList = []
    for x in data:
        if("src=".encode() in x):
            imageList.append(x)
    return imageList