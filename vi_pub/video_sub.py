#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2



class VideoSubscriber(Node):

	def __init__(self):
		super().__init__('video_subscriber')
		
		# Create the subscriber.
		self.subscription = self.create_subscription(Image, 'video_frames', self.listener_callback, 10)
		
		# Used to convert between ROS and OpenCV images
		self.bridge = CvBridge()
		
	def listener_callback(self, data):

		# display the message on the console
		self.get_logger().info('Receiving video frame')
		
		# Convert ROS Image message to OpenCV image
		current_frame = self.bridge.imgmsg_to_cv2(data)
		
		# Display image
		cv2.imshow("video", current_frame)
		cv2.waitKey(1)
		
		
		
def main(args=None):
	
	# Initialize the rclpy library
	rclpy.init(args=args)
	
	# Create the node
	video_sub = VideoSubscriber()
	
	# Spin the node so the callback function is called
	rclpy.spin(video_sub)
	
	# Destroy the node explicitly
	video_sub.destroy_node()
	
	# Shutdown the ROS client library for python
	rclpy.shutdown()


if __name__=='__main__':
	main()
	


