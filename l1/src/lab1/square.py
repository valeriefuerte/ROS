#! /usr/bin/python

import rospy
from geometry_msgs.msg import Twist
import math
import time

def move_forward(pub, msg, vel):
	msg.linear.x = vel
	msg.angular.z = 0.0
	pub.publish(msg)

def move_rotate(pub, msg):
	msg.linear.x = 0
	msg.angular.z= math.pi/2.0
	pub.publish(msg)

rospy.init_node('name_by_default')
pub1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 1)

vel = float(rospy.get_param('speed')

msg = Twist()
time.sleep(1)

r = rospy.Rate(0.5) #Hz 

while not rospy.is_shutdown():
	move_forward(pub1, msg, vel)
	time.sleep(1)
	move_rotate(pub1, msg)
	r.sleep()

