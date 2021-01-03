import urllib.request as url
import webbrowser

imageTypeList = [".jpg", ".png"]

def getUrlFromImgLine(line):
    splitString = str(line).split('"')
    for x in splitString:
        for type in imageTypeList:
            if(type in x):
                return x

def getDataFromUrl(myUrl):
    res = url.urlopen(myUrl)
    data = res.readlines()
    return data

def getImagePaths(data):
    imageList = []
    for x in data:
        if("<img src=".encode() in x):
            imageList.append(x)
    return imageList

def openWebsite(url):
    webbrowser.open(url)