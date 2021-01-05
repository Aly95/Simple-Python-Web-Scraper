# Application used to scrape my portfolio for images, and opens their path in a new browser tab

import WebScraper
from Image import Image

myUrl = "https://aly95.github.io/"
customUrl = "https://www.gettyimages.co.uk/collections/500px"

def main():
    imageList = []

    webData = WebScraper.getDataFromUrl(customUrl)

    unformattedImageList = WebScraper.getImageList(webData)

    for unformattedImage in unformattedImageList:
        formattedImage = WebScraper.getUrlFromImgLine(unformattedImage)
        imageList.append(formattedImage)

    for image in imageList:
        WebScraper.openWebsite(image, customUrl)

main()