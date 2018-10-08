#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
move = Twist()
move.linear.x = 0.5 #Move the robot with a linear velocity in the x axis
move.angular.z = 0.5 #Move the with an angular velocity in the z axis

while not rospy.is_shutdown(): 
  pub.publish(move)
  rate.sleep()