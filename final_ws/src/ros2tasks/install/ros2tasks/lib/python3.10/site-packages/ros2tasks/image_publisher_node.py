import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 as cv
class ImagePublisherNode(Node):
    def __init__(self):
        super().__init__('image_publisher_node')
        self.publisher_ = self.create_publisher(Image, '/camera', 10)
        self.timer = self.create_timer(1.0, self.timer_callback) 
        self.get_logger().info('image publisher node started')
    def timer_callback(self):
        cv_image=cv.imread('/home/kiara/final_ws/src/ros2tasks/ros2tasks/blucircle.png')
        print(type(cv_image))
        self.bridge = CvBridge()
        img = self.bridge.cv2_to_imgmsg(cv_image, encoding='passthrough')
        self.publisher_.publish(img)
        self.get_logger().info('published image to /camera')
def main(args=None):
    rclpy.init(args=args)
    image_publisher_node=ImagePublisherNode()
    rclpy.spin(image_publisher_node)
    image_publisher_node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()
