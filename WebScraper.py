import urllib.request as url
import re
import webbrowser
from Image import Image

imageTypeList = [".jpg", ".png"]
imageTagList = ["href", "src"]

# Retrieves and returns the data from the URL using the urllib module
def getDataFromUrl(myUrl: str):
    res = url.urlopen(myUrl)
    data = res.readlines()
    return data

# Searches the data for an image, and returns the line if found
def getImageList(data: str) -> list:
    imageList = []
    for line in data:
        if(checkValidImage(line)):
            image = convertToImageObject(line)
            imageList.append(image)
    return imageList

# Checks if the line contains any common HTML image tags
def checkForImageTags(line: str) -> bool:
    tagCheck = False
    for tag in imageTagList:
        if(tag.encode() in line):
            tagCheck = True
    return tagCheck

# Checks if the line contains any of the image formats contained in the image type list
def checkValidImage(line: str) -> bool:
    validImage = False
    for type in imageTypeList:
        if type.encode() in line:
            for tag in imageTagList:
                if tag.encode() in line:
                    validImage = True
    return validImage
            
def convertToImageObject(line: str) -> Image:
    if "href".encode() in line:
        return Image(line, 1)
    if "src".encode() in line:
        return Image(line, 2)

# Retrieves a list of all data within quotation marks
def getUrlFromImgLine(image: Image):
    path = str(image.path)
    dataWithinQuotationMarks = re.findall(r'"(.*?)(?<!\\)"', path) # Creates a list of strings of lines between quotation marks
    for x in dataWithinQuotationMarks:
        for type in imageTypeList:
            if(type in x):
                updatedImage = Image(x, image.type)
                return updatedImage

# Opens the given URL using the webbrowser module
def openWebsite(image: Image, url: str):
    if image.type == 2:
        url = url+image.path
    webbrowser.open(url)

# Searches the data for an image, and returns the line if found
def getImagePathsClone(data: str):
    imageList = []
    for x in data:
        if("src=".encode() in x):
            imageList.append(x)
    return imageList