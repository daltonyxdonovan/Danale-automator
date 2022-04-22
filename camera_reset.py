
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
flag = 0
url = "http://www.google.com"
getListError = "novideo.png"
logins = "login.png"
fault = "fault.png"
ready = "ready.png"
bug = "danalelogo.png"
bug2 = "novideo_small.png"
Devices = True
screen = (400,200,1100,700)
readyArea = (490, 420, 185, 80)
bugarea1 = (530,260,370,140)
bugarea2 = (1330,260,350,140)
bugarea3 = (500,700,400,200)
bugarea4 = (1340,700,400,200)

def detectReady():
    def refreshToggle(durations):
        pg.moveTo(668, 304, durations/5)
        pg.click()
    time.sleep(3)
    print("\n")
    print("Attempting to detect Danale ready state...")
    try:
        pg.locateOnScreen(ready, screen, confidence=0.5)
        print("Danale is ready!")
        return True
    except:
        print("Danale is not ready!")
        try:
            pg.locateOnScreen(bug2, screen, confidence=0.5)
            print("Danale is bugged, refreshing toggle...")
            refreshToggle(speed)
            return False
        except:
            print("Danale is not ready!")
            return False

def detectBug():
    time.sleep(5)
    print("Attempting to detect Danale ready state...")
    try:
        pg.locateOnScreen(bug, bugarea1, confidence=0.5)
        pg.locateOnScreen(bug, bugarea2, confidence=0.5)
        pg.locateOnScreen(bug, bugarea3, confidence=0.5)
        pg.locateOnScreen(bug, bugarea4, confidence=0.5)
        print("Danale is bugged, refreshing again...")
        return True
    except:
        return False

def detectInternet(durations):
    print("\n")
    print("Attempting to detect internet connection...")
    global internet
    global internetJustOff
    try:
        requests.get(url, timeout=durations*2)
        internet = True
        print("Internet connection detected!")
    except requests.ConnectionError:
        internet = False
        internetJustOff = True
        print("No internet connection detected!")

def minimizeVSCode(durations):
    print("Minimizing VSCode")
    pg.moveTo(1800, 20, durations/5)
    pg.click()

def loginCheck(durations):
    global justStarted
    try:
        pg.locateOnScreen(logins, screen, confidence = 0.5)
        print("Logging in to Danale")
        pg.moveTo(945,699, durations/5)
        pg.click()
        justStarted = False
        
    except:
        print("Passed Login Check")

def startFromDesktop(durations):
    global startTime
    pg.moveTo(20, 20, durations/5)
    print("Starting Danale from desktop shortcut at " + currentTime)
    startTime = time.time()
    pg.doubleClick()

def refreshMinimized(durations):
    print("Refreshing minimized Danale")
    pg.moveTo(650, 400, durations/5)
    pg.doubleClick()

def checkForDevices(durations):
    global Devices
    try:
        pg.locateOnScreen(getListError, screen, confidence=0.5)
        print("Cannot find devices! Retrying...")
        pg.moveTo(668, 304, durations/5)
        pg.click()
    except:
        print("Passed Device-Check")
        Devices = True
        
def Maximize(durations):
    print("Maximizing Danale")
    pg.moveTo(1430, 250, durations/5)
    pg.click()

def networkFaultAccept(durations):
    print("Accepting network fault...")
    pg.moveTo((1920/2)+120, (1080/2)+20, durations/5)
    pg.click()

def refreshToggle(durations):
    pg.moveTo(668, 304, durations/5)
    pg.click()

def refreshToggleMaximized(durations):
    time.sleep(2)
    pg.moveTo(238, 74, durations/5)
    pg.click()
    time.sleep(2)

def refreshMaximized(durations):
    print("Refreshing Danale at " + currentTime)
    pg.moveTo(150, 150, durations/5)
    pg.doubleClick()

def stopMaximized(durations):
    print("Stopping Danale at " + currentTime)
    print("\n")
    pg.moveTo(1900, 40, durations/5)
    pg.click()
    pg.moveTo((1920/2)+30, (1080/2)+20, durations/5)
    pg.click()
    
while running:
    currentTime = time.strftime("%H:%M:%S")
    if internet == False:
        justStarted = True
        flag = 0
        networkFaultAccept(speed)
        print("Check failed. Retrying in 120 seconds...")
        time.sleep(120)
        detectInternet(speed)
    if justStarted == True and internet == True:
        if flag == 0:
            loginCheck(speed)
            startFromDesktop(speed)
            flag = 1
        if flag == 1:
            if detectReady() == True:
                loginCheck(speed)
                refreshMinimized(speed)
                Maximize(speed)
                justStarted = False
            else:
                detectReady()
    if justStarted == False and internet == True:
        time.sleep(480)
        detectInternet(speed)
        refreshMaximized(speed)

        if detectBug() == True:
            refreshToggleMaximized(speed)
            refreshMaximized(speed)



    