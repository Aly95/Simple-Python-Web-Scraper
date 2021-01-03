# Application used to scrape my portfolio for images, and opens each path in a new browser tab

import WebScraper as web

myUrl = "https://aly95.github.io/"

def main():
    imageList = []

    data = web.getDataFromUrl(myUrl)
    scrapedImageSrcLines = web.getImagePaths(data)

    for line in scrapedImageSrcLines:
        retrievedImagePath = web.getUrlFromImgLine(line)
        imageList.append(retrievedImagePath)

    for image in imageList:
        web.openWebsite(myUrl + image)

main()