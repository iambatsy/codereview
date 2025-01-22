import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class VisionDetector:
    def __init__(self):
        self.area = 0

    def detect_shapes(self,img):
        shapes=set()
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        
        canny=cv.Canny(gray,125,175)
        contours,hiearchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
        #cv.imshow('c',canny)
        for contour in contours:
            approx=cv.approxPolyDP(contour,0.02*cv.arcLength(contour,True),True)
            cv.drawContours(img, approx, -1, (0,255,0), 3)
            cv.imshow("kys", img)
            if len(approx) == 3:
                shapes.add(("Triangle"))
            elif len(approx) == 4:
                shapes.add(("Square"))
            elif len(approx) > 5:
                shapes.add(("Circle"))
           
         
            return shapes

    def detect_color(self,img):
        hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
        lower_blue=np.array([110,50,50])
        upper_blue=np.array([130,255,255])
        mask=cv.inRange(hsv,lower_blue,upper_blue)
        
        result=cv.bitwise_and(img,img,mask=mask)
        ##print(mask , "mask ")
        c , h = cv.findContours(mask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for cs in c:
            self.area = cv.contourArea(cs)
       
        if(self.area > 3):
          cv.imshow("blue color detected",np.hstack([img,result]))
        else:
            print("not color vlue")
        
        
        
        return result
detector=VisionDetector()
img=cv.imread('/home/kiara/Downloads/image2/image2/blusquare.png')
shapes=detector.detect_shapes(img)
print ('Shapes detected are:' , shapes)
result=detector.detect_color(img)

##print (result, "SHAPES")
cv.waitKey(0)