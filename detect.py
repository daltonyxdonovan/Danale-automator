
import pyautogui as pg
import PIL
import time, requests, os

running = True
justStarted = True
speed = 5
internet = True

internetJustOff = False
tick = 0
subtick = 0
wipetick = 0
url = "http://www.google.com"
getListError = "novideo.png"
logins = "login.png"
fault = "fault.png"
ready = "ready.png"
Devices = True
screen = (400,200,1100,700)
readyArea = (490, 420, 675, 500)

def detectReady():
    print("\n")
    print("Attempting to detect Danale ready state...")
    try:
        pg.locateOnScreen(ready, readyArea, confidence=0.5)
        print("Danale is ready!")
        return True
    except:
        print("Danale is not ready!")
        return False

while running:
    tick += 1
    if tick > 1000:
        tick = 0
        subtick += 1
    if subtick == 1000:
        detectReady()
        subtick = 0