import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class VisionDetector:
    def __init__(self):
        pass
    def detect_shapes(self,img):
        shapes=[]
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        
        canny=cv.Canny(gray,125,175)
        contours,hiearchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            approx=cv.approxPolyDP(contour,0.02*cv.arcLength(contour,True),True)
            if len(approx) == 3:
                shapes.append(("Triangle", contour))
            elif len(approx) == 4:
                shapes.append(("Square", contour))
            elif len(approx) > 5:
                shapes.append(("Circle", contour))

        return shapes
    def detect_color(self,img):
        hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
        lower_blue=np.array([110,50,50])
        upper_blue=np.array([130,255,255])
        mask=cv.inRange(hsv,lower_blue,upper_blue)
        result=cv.bitwise_and(img,img,mask=mask)
        return result
detector=VisionDetector()
img=cv.imread('ros2tasks/blucircle.png')
shapes=detector.detect_shapes(img)
result=detector.detect_color(img)

print (shapes)
class VisionDetectorNode(Node):
    def __init__(self):
        super().__init__('vision_detector_node')
        self.image_subscriber = self.create_subscription(Image, '/camera', self.image_callback, 10)
        self.detections_publisher = self.create_publisher(String, '/detections', 10)
        self.get_logger().info("started")
    

def main(args=None):
    rclpy.init(args=args)
    vision_detector_node=VisionDetectorNode()
    rclpy.spin(vision_detector_node)
    vision_detector_node.destroy_node()
    rclpy.shutdown
if __name__=='__main__':
    main()
 

