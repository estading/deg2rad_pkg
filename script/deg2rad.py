#!/usr/bin/env python3
import math
import rospy
from std_msgs.msg import Float32
count = 0
def receive_news_cb(msg):
    global count
    count += 1
    rad = msg.data*(math.pi/180)
    rospy.loginfo(f'Degrees: {msg.data} Radians: {rad}, {count}')

if __name__ == '__main__':
    rospy.init_node('deg2rad')
    sub = rospy.Subscriber('/deg_topic', Float32, receive_news_cb)
    rospy.spin()
