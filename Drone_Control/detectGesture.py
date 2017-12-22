import numpy as np
import cv2

def detectHandGesture(img):
    #this is the cascade we just made. Call what you want
    fist_cascade = cv2.CascadeClassifier('Fist.xml') # 100 % Accurancy
    palm_cascade = cv2.CascadeClassifier('Palm.xml')
    v_cascade = cv2.CascadeClassifier('V.xml')
    litf_cascade = cv2.CascadeClassifier('LittleFinger.xml')
    g_symbol_cascade = cv2.CascadeClassifier('LittleFinger.xml')


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # add this
    # image, reject levels level weights.
    fist = fist_cascade.detectMultiScale(gray, 1.5,5)
    palm = palm_cascade.detectMultiScale(gray, 1.5,5)
    v_symbol = v_cascade.detectMultiScale(gray, 1.5,5)
    #litf = litf_cascade.detectMultiScale(gray, 1.5,5)
    detected_gesture = '' 
    for (x,y,w,h) in fist:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        detected_gesture = 'Fist'

    for (x,y,w,h) in palm:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        detected_gesture = 'Palm'
    for (x,y,w,h) in v_symbol:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        detected_gesture = "V_Symbol"

    for (x,y,w,h) in v_symbol:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        detected_gesture = "G_Symbol"

    for (x,y,w,h) in litf:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
        detected_gesture = "LittleFinger"
    
    cv2.imshow('img',img)
    cv2.waitKey(100)
    cv2.destroyAllWindows()
    return detected_gesture
