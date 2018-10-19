#! /usr/bin/env python
import rospy
import time
import actionlib

from actionlib.msg import TestFeedback, TestResult, TestAction
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class MoveSquareClass(object):
    
  # create messages that are used to publish feedback/result
  _feedback = TestFeedback()
  _result   = TestResult()

  def __init__(self):
    # creates the action server
    self._as = actionlib.SimpleActionServer("move_drone_square_as", TestAction, self.goal_callback, False)
    self._as.start()
    self.ctrl_c = False
    self.rate = rospy.Rate(10)
    
  
  def publish_once_in_cmd_vel(self, cmd):
    """
    This is because publishing in topics sometimes fails teh first time you publish.
    In continuos publishing systems there is no big deal but in systems that publish only
    once it IS very important.
    """
    while not self.ctrl_c:
        connections = self._pub_cmd_vel.get_num_connections()
        if connections > 0:
            self._pub_cmd_vel.publish(cmd)
            rospy.loginfo("Publish in cmd_vel...")
            break
        else:
            self.rate.sleep()
            
  # function that stops the drone from any movement
  def stop_drone(self):
    rospy.loginfo("Stopping...")
    self._move_msg.linear.x = 0.0
    self._move_msg.angular.z = 0.0
    self.publish_once_in_cmd_vel(self._move_msg)
        
  # function that makes the drone turn 90 degrees
  def turn_drone(self):
    rospy.loginfo("Turning...")
    self._move_msg.linear.x = 0.0
    self._move_msg.angular.z = 1.0
    self.publish_once_in_cmd_vel(self._move_msg)
    
  # function that makes the drone move forward
  def move_forward_drone(self):
    rospy.loginfo("Moving forward...")
    self._move_msg.linear.x = 1.0
    self._move_msg.angular.z = 0.0
    self.publish_once_in_cmd_vel(self._move_msg)
    
  def goal_callback(self, goal):
    # this callback is called when the action server is called.
    # this is the function that computes the Fibonacci sequence
    # and returns the sequence to the node that called the action server
    
    # helper variables
    r = rospy.Rate(1)
    success = True
    
    # define the different publishers and messages that will be used
    self._pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    self._move_msg = Twist()
    self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
    self._takeoff_msg = Empty()
    self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)
    self._land_msg = Empty()
    
    # make the drone takeoff
    i=0
    while not i == 3:
        self._pub_takeoff.publish(self._takeoff_msg)
        rospy.loginfo('Taking off...')
        time.sleep(1)
        i += 1
    
    # define the seconds to move in each side of the square (which is taken from the goal) and the seconds to turn
    sideSeconds = goal.goal
    turnSeconds = 1.8
    
    i = 0
    for i in xrange(0, 4):
    
      # check that preempt (cancelation) has not been requested by the action client
      if self._as.is_preempt_requested():
        rospy.loginfo('The goal has been cancelled/preempted')
        # the following line, sets the client in preempted state (goal cancelled)
        self._as.set_preempted()
        success = False
        # we end the calculation of the Fibonacci sequence
        break
    
      # Logic that makes the robot move forward and turn
      self.move_forward_drone()
      time.sleep(sideSeconds)
      self.turn_drone()
      time.sleep(turnSeconds)
      
      # build and publish the feedback message
      self._feedback.feedback = i
      self._as.publish_feedback(self._feedback)
      # the sequence is computed at 1 Hz frequency
      r.sleep()
    
    # at this point, either the goal has been achieved (success==true)
    # or the client preempted the goal (success==false)
    # If success, then we publish the final result
    # If not success, we do not publish anything in the result
    if success:
      self._result.result = (sideSeconds*4) + (turnSeconds*4)
      rospy.loginfo('The total seconds it took the drone to perform the square was %i' % self._result.result )
      self._as.set_succeeded(self._result)
        
      # make the drone stop and land
      self.stop_drone()
      i=0
      while not i == 3:
          self._pub_land.publish(self._land_msg)
          rospy.loginfo('Landing...')
          time.sleep(1)
          i += 1
      
if __name__ == '__main__':
  rospy.init_node('move_square')
  MoveSquareClass()
  rospy.spin()