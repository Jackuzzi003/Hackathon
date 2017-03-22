#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


class example(object):
    #constructor
    def __init__(self):
        pass
    # Function to controll the Robot
    def position(self): 
        rospy.Subscriber("/odom",Odometry,self.call)                            # subscribe to the Odometry topic
        y = raw_input('please enter start or stop: ')                           # get Input for starting and stopping, not really needed in the final program, but here it is left to give the Subscriber some time, otherwise it would give an error
        pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10)                 # initializing pub to be a Publisher to the cmd_vel topic
        a = self.b                                                              # saving the current position for distance measurement
        twist = Twist()                                                         # creating the Twist variable to publish the velocity later
        if y == 'start':                                                        
            x = raw_input('please enter left or right: ')                       # getting Input for the direction to move 
            z = raw_input('please enter velocity: ')                            # getting the velocity at which the robot should move
            d = raw_input('please enter distance: ')                            # getting the distance 
            d = float(d)                                                        # converting str(d) to float(d)
            if x == 'left':                                                         
                while self.b < a+d:                                             # run this as long as the y value of the robots current position is smaller than the starting position added to the wanted distance
                    twist.linear.y= float(z)    
                    pub.publish(twist)                                          # publishing the velocity command to the cmd_vel topic
                twist.linear.y = 0.0                                            # stopping the robot after the distance has been driven
                pub.publish(twist)
                        
            elif x == 'right':                                                  # same as 'left' only for 'right', so the signs have to be inverted
                while self.b > a-d:
                    twist.linear.y = -float(z)
                    print(' b ' + str(self.b) + ' pos ' + str(a-d))
                    pub.publish(twist)
                twist.linear.y = 0.0
                pub.publish(twist) 
                
        elif y =='stop':                                                        # stop condition is not needed
            
            twist.linear.y = 0.0
            pub.publish(twist)
        print("done")    
        
    def call(self,msg):                                                         
        self.b = msg.pose.pose.position.y                                       # getting the y value of the robots position from the topic /odom and assigning it to b
        
        
    
if __name__ == '__main__':
    rospy.init_node('anyname')
    obj1 = example()                                                            # creating an object of the class that has been made
    while not rospy.is_shutdown():
        obj1.position()                                                         # running the function to move the robot
        #rospy.spin()