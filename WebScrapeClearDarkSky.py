from bs4 import BeautifulSoup as soup
import requests

Cloud_Cover = []
Transparency = []
Seeing = []
Darkness = []
Wind = []
Humidity = []
Temperature = []

html_file = requests.get('http://www.cleardarksky.com/c/HptngSPNJkey.html?1')
soup = soup(html_file.content, 'lxml')


def getWeatherData(startBlock, endBlock):
    x = 1
    for area in soup.find_all("area"):
        if x >= startBlock and x <= endBlock:
            Cloud_Cover.append(area.get("title"))
        elif x >= startBlock + 46 and x <= endBlock + 46:
            Transparency.append(area.get("title"))
        elif x >= startBlock + 92 and x <= endBlock + 92:
            Seeing.append(area.get("title"))
        elif x >= startBlock + 138 and x <= endBlock + 138:
            Wind.append(area.get("title"))
        elif x >= startBlock + 184 and x <= endBlock + 184:
            Humidity.append(area.get("title"))
        elif x >= startBlock + 230 and x <= endBlock + 230:
            Temperature.append(area.get("title"))        
        x += 1


def getTimeRef():
    x = 1
    time = ""
    timeTextHolder = []
    for font in soup.find_all('font'):
        if x == 7:
            timeTextHolder = font.text.split(" ")
        x += 1
    time = timeTextHolder[3]
    time = int(time[:2])
    return time


def getWeatherData2(startTime, endTime):
    timeRef = getTimeRef()

    startBlock = (startTime - timeRef) + 1
    if endTime < 24 and endTime > startTime:
        endBlock = (endTime - timeRef) + 1
    elif endTime < startTime:
        endBlock = 25 + (endTime - timeRef)
    else:
        print("Error in getWeatherData2: Times")

    if endBlock <= 46:
        getWeatherData(startBlock, endBlock)
        printWeatherData(startTime, endTime)
    else:
        print("I cant see that far in the future")


def printWeatherData(startTime, endTime):
    y = 0
    z = 0
    for x in Cloud_Cover:
        if startTime + y <= 23 and y >= 0:
            print(str(startTime + y) + ": " + x)
            y += 1
        else:
            print(str(z) + ": " + x)
            z += 1
            
    y = 0
    z = 0
    for x in Transparency:
        if startTime + y <= 23 and y >= 0:
            print(str(startTime + y) + ": " + x)
            y += 1
        else:
            print(str(z) + ": " + x)
            z += 1

    y = 0
    z = 0
    for x in Seeing:
        if startTime + y <= 23 and y >= 0:
            print(str(startTime + y) + ": " + x)
            y += 1
        else:
            print(str(z) + ": " + x)
            z += 1

    y = 0
    z = 0
    for x in Wind:
        if startTime + y <= 23 and y >= 0:
            print(str(startTime + y) + ": " + x)
            y += 1
        else:
            print(str(z) + ": " + x)
            z += 1

    y = 0
    z = 0
    for x in Humidity:
        if startTime + y <= 23 and y >= 0:
            print(str(startTime + y) + ": " + x)
            y += 1
        else:
            print(str(z) + ": " + x)
            z += 1

    y = 0
    z = 0
    for x in Temperature:
        if startTime + y <= 23 and y >= 0:
            print(str(startTime + y) + ": " + x)
            y += 1
        else:
            print(str(z) + ": " + x)
            z += 1

