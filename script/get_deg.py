#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

if __name__ == '__main__':
	rospy.init_node('get_deg')
	pub = rospy.Publisher('/deg_topic', Float32, queue_size = 10)
	
	rate = rospy.Rate(0.2)
	while not rospy.is_shutdown():
		msg = Float32()
		msg.data = rospy.get_param("/degrees")
		pub.publish(msg)
		rate.sleep()
	rospy.loginfo('Node stopped')
