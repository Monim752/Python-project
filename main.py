import cv2
import numpy as np
import pyautogui

capture=cv2.VideoCapture(0)
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
pre_y=0;
while True:
    ret, box=capture.read()
    color=cv2.cvtColor(box, cv2.COLOR_BGR2HSV)
    musk=cv2.inRange(color, lower_red, upper_red)
    contours, hierarchy=cv2.findContours(musk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for con in contours:
        area=cv2.contourArea(con)
        if area>500:
            x,y,w,z=cv2.boundingRect(con)
            cv2.rectangle(box, (x,y), (x+w,y+z),(0, 255, 0) ,2)
            if pre_y>y:
                pyautogui.press('space')
            pre_y=y

    cv2.imshow('box', box)
    if cv2.waitKeyEx(20)==ord('s'):
        break

capture.release()
cv2.destroyWindow()