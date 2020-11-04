#! /usr/bin/python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

import time
import math


class Main:
    def __init__(self):
	self.pose = Pose()

        self.pub = rospy.Publisher('/turtle_2/cmd_vel', Twist, queue_size=1)
	self.sub1 = rospy.Subscriber('/turtle_1/pose', Pose, self.follow)
	self.sub2 = rospy.Subscriber('/turtle_2/pose', Pose, self.updatePose)

        self.rate = rospy.Rate(10)

    def updatePose(self, data):	
        self.pose = data

    def calc_distance(self, x, y):
        distance = math.sqrt(math.pow((x - self.pose.x), 2) + math.pow((y - self.pose.y), 2))
        return distance

    def calc_angle(self, x, y):
        angle = math.atan2(y - self.pose.y, x - self.pose.x)
	result = angle - self.pose.theta
        return result

    def follow(self, msg):
	if self.pose is not None:
		twist = Twist()
		twist.linear.x = 0.5 * self.calc_distance(msg.x, msg.y)
		twist.angular.z = 2 * self.calc_angle(msg.x, msg.y)

		self.pub.publish(twist)


rospy.init_node('main')	    

x = Main()
rospy.spin()
   
