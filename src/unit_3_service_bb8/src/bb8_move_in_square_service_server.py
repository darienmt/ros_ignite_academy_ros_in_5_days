#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from move_bb8 import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_square has been called")
    movebb8_object = MoveBB8()
    movebb8_object.move_square()
    rospy.loginfo("Finished service move_bb8_in_square that was called called")
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('service_move_bb8_in_square_server') 
my_service = rospy.Service('/move_bb8_in_square', Empty , my_callback) # create the Service called move_bb8_in_square with the defined callback
rospy.loginfo("Service /move_bb8_in_square Ready")
rospy.spin() # mantain the service open.