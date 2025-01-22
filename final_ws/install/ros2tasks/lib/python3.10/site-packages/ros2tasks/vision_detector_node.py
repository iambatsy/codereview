import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from cv_bridge import CvBridge

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
            
            
            if len(approx) == 3:
                shapes.add(("Triangle"))
            elif len(approx) == 4:
                shapes.add(("Square"))
            elif len(approx) > 5:
                shapes.add(("Circle"))
        #cv.imshow("image", img)
        cv.waitKey(0)
           
         
        return shapes

    def detect_color(self,img):
        hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
        lower_blue=np.array([110,50,50])
        upper_blue=np.array([130,255,255])
        mask=cv.inRange(hsv,lower_blue,upper_blue)
        
        result=cv.bitwise_and(img,img,mask=mask)
        #print(mask , "mask ")
        c , h = cv.findContours(mask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for cs in c:
            self.area = cv.contourArea(cs)
       
        if(self.area > 3):
          print('blue color detected')
        else:
            print("not color vlue")
    
        
        
        return result


class VisionDetectorNode(Node):
    def __init__(self):
        super().__init__('vision_detector_node')
        self.bridge=CvBridge()
        self.image_subscriber = self.create_subscription(Image, '/camera', self.image_callback, 10)
        self.detections_publisher = self.create_publisher(String, '/detections', 10)
        self.timer = self.create_timer(1.0, self.timer_callback) 
        self.detector=VisionDetector()
        #img=cv.imread('/home/kiara/Downloads/image2/image2/blusquare.png')
        self.shapes =""
        
         
    def image_callback(self,msg):
        
        img=self.bridge.imgmsg_to_cv2(msg)
        self.shapes=self.detector.detect_shapes(img)
        self.shapes = str(self.shapes)
        print(type(self.shapes))
        #print ('Shapes detected are:' , shapes)
        result=self.detector.detect_color(img)
        
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %s' % self.shapes
        self.detections_publisher.publish(msg) 
    

def main(args=None):
    rclpy.init(args=args)
    vision_detector_node=VisionDetectorNode()
    rclpy.spin(vision_detector_node)
    vision_detector_node.destroy_node()
    rclpy.shutdown
if __name__=='__main__':
    main()
 

