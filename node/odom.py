#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class odom(object):
    def __init__(self,b):
        b = msg.pose.pose.position.y
        
def call(msg):
#==============================================================================
#         global b
#         b = msg.pose.pose.position.y
#==============================================================================
    
def position():
    #global b
    rospy.init_node('odom')
    
    rospy.Subscriber("odom", Odometry, call)
    
    print yannick.b
    
if __name__ == '__main__':
    yannick = odom()
    
    try:
        while not rospy.is_shutdown():
            position()  
    except rospy.ROSInterruptException:
        pass 