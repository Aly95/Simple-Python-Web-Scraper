import urllib.request as url
import re
import webbrowser

imageTypeList = [".jpg", ".png"]

# Retrieves a list of all data within quotation marks
def getUrlFromImgLine(line):
    dataWithinQuotationMarks = re.findall(r'"(.*?)(?<!\\)"', line)
    for x in dataWithinQuotationMarks:
        for type in imageTypeList:
            if(type in x):
                return x

# Retrieves and returns the data from the URL using the urllib module
def getDataFromUrl(myUrl):
    res = url.urlopen(myUrl)
    data = res.readlines()
    return data

# Searches the data for an image, and returns the line if found
def getImagePaths(data):
    imageList = []
    for x in data:
        if("<img src=".encode() in x):
            imageList.append(x)
    return imageList

# Opens the given URL using the webbrowser module
def openWebsite(url):
    webbrowser.open(url)