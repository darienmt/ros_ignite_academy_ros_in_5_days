#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist

turn_velocity = 0.9
linear_velocity = 1.
first_turn_distance = 1
second_turn_distance = 0.4

def callback(msg): 
  #print msg.ranges[360] #We print the distance to an obstacle in front of the robot

#If the distance to an obstacle in front of the robot is bigger than 1 meter, the robot will move forward
  if msg.ranges[360] > first_turn_distance:
      move.linear.x = linear_velocity
      move.angular.z = 0.0

#If the distance to an obstacle in front of the robot is smaller than 1 meter, the robot will turn left
  if msg.ranges[360] < 1: 
      move.linear.x = linear_velocity/10.
      move.angular.z = turn_velocity
        
#If the distance to an obstacle at the left side of the robot is smaller than 0.3 meters, the robot will turn right
  if msg.ranges[719] < second_turn_distance:
      move.linear.x = linear_velocity/10.
      move.angular.z = -turn_velocity
        
#If the distance to an obstacle at the right side of the robot is smaller than 0.3 meters, the robot will turn left
  if msg.ranges[0] < second_turn_distance:
      move.linear.x = linear_velocity/10.
      move.angular.z = turn_velocity
      
  pub.publish(move)

rospy.init_node('sub_node')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()