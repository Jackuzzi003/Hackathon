#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from Odometry_msgs.msg import Odometry



def call(msg):
    print("hi")
    return msg.pose.pose.position.y

def position():
        y = raw_input('please enter start or stop: ')
        rospy.init_node('ourrobot')
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10)
        rospy.Subscriber("/odom", Odometry, call)
        twist = Twist()
        if y == 'start':
            x = raw_input('please enter left or right: ')
            z = raw_input('please enter velocity: ')
            
            if x == 'left':
                twist.linear.y= float(z)
                print('left')
                
            elif x == 'right':
                twist.linear.y = -float(z)
                print('right')
                
            pub.publish(twist)
        elif y =='stop':
            
            twist.linear.y = 0.0
            pub.publish(twist)
        
    
if __name__ == '__main__':
    try:
        
            position()  
            rospy.spin()
    except rospy.ROSInterruptException:
        pass 