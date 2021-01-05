# Application used to scrape my portfolio for images, and opens their path in a new browser tab

import WebScraper
from Image import Image

myUrl = "https://aly95.github.io/"
ytUrl = "https://www.gettyimages.co.uk/collections/500px"

def main():
    imagePathList = []

    webData = WebScraper.getDataFromUrl(ytUrl)

    unformattedImageList = WebScraper.getImageList(webData)

    for unformattedImage in unformattedImageList:
        imagePath = WebScraper.getUrlFromImgLine(unformattedImage)
        imagePathList.append(imagePath)

    for path in imagePathList:
        print(path.path)
        WebScraper.openWebsite(path, ytUrl)

main()