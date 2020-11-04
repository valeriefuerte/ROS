#! /usr/bin/python

import rospy
from geometry_msgs.msg import Twist
import time
import math

def move_forward(pub, msg):
    msg.linear.x = 4.0
    msg.angular.z = 0.0
    pub.publish(msg)

def move_rotate(pub, msg):
    msg.linear.x = 0.0
    msg.angular.z = math.pi/2
    pub.publish(msg)

rospy.init_node('name_by_default')

pub1 = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
pub2 = rospy.Publisher('leonardo/cmd_vel', Twist, queue_size=1)
msg = Twist()

r = rospy.Rate(0.5) #Hz

while not rospy.is_shutdown():
    move_forward(pub1, msg)
    move_forward(pub2, msg)

    time.sleep(1)

    move_rotate(pub1, msg)
    move_rotate(pub2, msg)

    r.sleep()

