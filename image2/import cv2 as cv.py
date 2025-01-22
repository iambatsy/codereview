import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class VisionDetector:
    def __init__(self):
        pass
    def detect_shapes(self,img):
        shapes=set()
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        
        
        canny=cv.Canny(gray,125,175)
        cv.imshow('canny',canny)
        contours,hiearchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
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
           
            area=cv.contourArea(contour)
            
            # if a
            # pass   
            return shapes

detector=VisionDetector()
img=cv.imread('./blusquare.png')
shapes=detector.detect_shapes(img)
print ('Shapes detected are:' , shapes)
cv.waitKey(0)
    
