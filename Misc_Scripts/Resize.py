import os 
import cv2
counter = 1
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
    	image = cv2.imread(filename,0)
    	resized = cv2.resize(image, (100, 100), interpolation = cv2.INTER_AREA)
    	cv2.imwrite("V"+str(counter)+".jpg", resized)
        print "V"+str(counter)+".jpg"
        counter += 1
    else:
        continue