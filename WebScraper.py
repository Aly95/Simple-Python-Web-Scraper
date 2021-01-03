import urllib.request as url
import webbrowser

imageTypeList = [".jpg", ".png"]

# Splits the passed string at each ", and runs through the split strings until it finds a line with .jpg or .png, returning it
def getUrlFromImgLine(line):
    splitString = str(line).split('"')
    for x in splitString:
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