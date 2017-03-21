#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def position():
    
        rospy.loginfo('please enter')
        x = raw_input()
        rospy.init_node('ourrobot')
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10)
        
        twist = Twist() 
        
        if x == 'left':
            twist.linear.y= 0.25
            rospy.loginfo('left')
        elif x == 'right':
            twist.linear.y = -0.25
            rospy.loginfo('right')
        pub.publish(twist)
    
        
    
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            position()  
    except rospy.ROSInterruptException:
        pass 