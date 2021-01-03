# Application used to scrape my portfolio for images, and opens each path in a new browser tab

import WebScraper as web

myUrl = "https://aly95.github.io/"

def main():
    imageList = []

    data = web.getDataFromUrl(myUrl)
    scrapedImageSrcLines = web.getImagePaths(data)

    for line in scrapedImageSrcLines:
        lineConvertedToString = str(line)
        retrievedImagePath = web.getUrlFromImgLine(lineConvertedToString)
        imageList.append(retrievedImagePath)

    for image in imageList:
        print(image)
        #web.openWebsite(myUrl + image)

main()