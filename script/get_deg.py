#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
def pull_degree():
	rospy.init_node('get_deg', anonymous=True)
	pub = rospy.Publisher('/deg_topic', Float32, queue_size = 10)
	rate = rospy.Rate(0.2)
	while not rospy.is_shutdown():
		msg = Float32()
		msg.data = rospy.get_param("/degrees")
		pub.publish(msg)
		rate.sleep()	

if __name__ == '__main__':
	try:
		pull_degree()
	except rospy.ROSInterruptException:
		pass
