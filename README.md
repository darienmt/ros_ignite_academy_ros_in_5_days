# ROS Ignite Academy : ROS in 5 Days projects

I am playing with ROS Ignite Academy and ROS. This repo will contain all the code I wrote there.

## Unit 1: Intro
- [my_package](src/my_package): The simplest package just to print "Help me Obi-Wan Kenobi, you're my only hope"... Why that sounds familiar.... ;-)

## Unit 2: Topics
- [read_odometry](src/read_odometry): Node subscribed to the odometry topic(/odom) and also compile a creates a message Age.
- [simple_topic_publisher](src/simple_topic_publisher): Publish velocity commands(Twist) to the /cmd_vel topic to move the robot.
- [topics_mini_project](src/topics_mini_project): Reads the laser scan messages(/kobuki/laser/scan) and command the robot to move avoiding hitting the wall.

## Unit 3: Services
- [simple_service_client.py](src/simple_service_client.py): A service client to delete an object from gazebo.
- [unit_3_services](src/unit_3_services): Create a node calling the /execute_trajectory service to move the arm on a trajectory in a file.
- [unit_3_service_bb8](src/unit_3_service_bb8): Create a services for moving a BB8 model in Gazebo on a square trajectory with fixed and custom square side.

## Unit 4: Actions
- [ardrone_action_client.py](src/ardrone_action_client.py): Simple action client.
- [exercise_46](src/exercise_46): Node to use the ARDrone action to move the drone.
- [cancel_goal_test.py](src/candel_goal_test.py): Action goal cancelation to see the effect on the action node.



