#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2


class VideoPublisher(Node):

	def __init__(self):
		super().__init__('video_publisher')
		
		# Create the publisher.
		self.publisher_ = self.create_publisher(Image, 'video_frames', 10)

		timer_period = 0.1 # second
		self.timer = self.create_timer(timer_period, self.timer_callback)
		
		# Create a VideoCapure ojbect
		video_file = '/home/sohee/ros2_ws/src/vi_pub/video/Cat.mp4'
		self.cap = cv2.VideoCapture(video_file);
		
		# Used to convert between ROS and OpenCV images
		self.bridge = CvBridge()
		
	def timer_callback(self):
		# Capture frame-by-frame
		ret, frame = self.cap.read()
		
		h, w = frame.shape[0], frame.shape[1]
		frame = cv2.resize(frame, (w//4, h//4))
		
		if ret:
			# Publish the image
			# cv2_to_imgmsg: convert an OpenCV image to a ROS 2 image message
			self.publisher_.publish(self.bridge.cv2_to_imgmsg(frame, 'bgr8'))
		
			# Display the messgae on the console
			self.get_logger().info('Publishing video frame')

			

def main(args=None):
	
	# Initialize the rclpy library
	rclpy.init(args=args)
	
	# Create the node
	video_pub = VideoPublisher()
	
	# Spin the node so the callback function is called
	rclpy.spin(video_pub)
	
	# Destroy the node explicitly
	video_pub.destroy_node()
	
	# Shutdown the ROS client library for python
	rclpy.shutdown()


if __name__=='__main__':
	main()
	


