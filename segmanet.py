import cv2
import os
vidcap = cv2.VideoCapture('room1.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        name = './input/frame' +  str(count)  + '.jpg'
        print('creating' +str(count))
        cv2.imwrite(name, image) 
        # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 1 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count  + 1
    sec = sec +  frameRate
    sec = round(sec, 2)
    success = getFrame(sec)