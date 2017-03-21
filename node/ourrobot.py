#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def position():
        print('please enter start or stop')
        y = raw_input()
        rospy.init_node('ourrobot')
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10)
        twist = Twist()
        if y == 'start':
            print('please enter left or right')
            x = raw_input()
            
            
            if x == 'left':
                twist.linear.y= 0.5
                print('left')
                
            elif x == 'right':
                twist.linear.y = -0.5
                print('right')
                
            pub.publish(twist)
        elif y =='stop':
            
            twist.linear.y = 0.0
            pub.publish(twist)
        
    
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            position()  
    except rospy.ROSInterruptException:
        pass 