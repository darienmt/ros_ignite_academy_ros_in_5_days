# ROS Ignite Academy : ROS in 5 Days projects

I am playing with ROS Ignite Academy and ROS. This repo will contain all the code I wrote there.

## Unit 1: Intro
- [my_package](src/my_package): The simplest package just to print "Help me Obi-Wan Kenobi, you're my only hope"... Why that sounds familiar.... ;-)

## Unit 2: Topics
- [read_odometry](src/read_odometry): Node subscribed to the odometry topic(/odom) and also compile a creates a message Age.
- [simple_topic_publisher](src/simple_topic_publisher): Publish velocity commands(Twist) to the /cmd_vel topic to move the robot.
- [topics_mini_project](src/topics_mini_project): Reads the laser scan messages(/kobuki/laser/scan) and command the robot to move avoiding hitting the wall.
