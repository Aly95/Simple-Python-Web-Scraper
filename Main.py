# Application used to scrape my portfolio for images, and opens their path in a new browser tab

import WebScraper

myUrl = "https://aly95.github.io/"

def main():
    imagePathList = []

    webData = WebScraper.getDataFromUrl(myUrl)

    imageList = WebScraper.getImageList(webData)

    for line in imageList:
        lineToString = str(line)
        imagePath = WebScraper.getUrlFromImgLine(lineToString)
        imagePathList.append(imagePath)

    for path in imagePathList:
        WebScraper.openWebsite(myUrl + path)

main()