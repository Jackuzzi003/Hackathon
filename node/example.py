#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


class example(object):
    #constructor
    def __init__(self):
        pass
    
    def position(self):
        rospy.Subscriber("/odom",Odometry,self.call)
        y = raw_input('please enter start or stop: ')
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10)
        a = self.b
        twist = Twist()
        if y == 'start':
            x = raw_input('please enter left or right: ')
            z = raw_input('please enter velocity: ')
            d = raw_input('please enter distance: ')
            d = float(d)
            if x == 'left':
                while self.b < a+d:
                    print("self.b")
                    twist.linear.y= float(z)
                    print('left')
                    pub.publish(twist)
                twist.linear.y = 0.0
                pub.publish(twist)
                        
            elif x == 'right':
                while self.b > a-d:
                    twist.linear.y = -float(z)
                    print(' b ' + str(self.b) + ' pos ' + str(a-d))
                    pub.publish(twist)
                twist.linear.y = 0.0
                pub.publish(twist) 
                
        elif y =='stop':
            
            twist.linear.y = 0.0
            pub.publish(twist)
        print("done")
        
    def function(self):
        pass
        #rospy.loginfo(self.b)
        #rospy.loginfo(self.b)
        
        
    def call(self,msg):
        self.b = msg.pose.pose.position.y
        
        
    
if __name__ == '__main__':
    rospy.init_node('anyname')
    obj1 = example()
    while not rospy.is_shutdown():
        obj1.position()
        #rospy.spin()