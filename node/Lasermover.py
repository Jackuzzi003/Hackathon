#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

def Scan(msg):
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10)
    min_scan = msg.ranges
    twist = Twist()
    min_scan = min(min_scan)
    print("minimum front ", min_scan)
    if min_scan < 0.40:
        twist.linear.x = -0.2
        pub.publish(twist)
        print(twist)
        
        if min_scan > 0.35 :
            rospy.sleep(1)
            twist.linear.x = 0.0
            pub.publish(twist)
    
def Scan_back(msg):
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 10)
    min_scan = msg.ranges
    twist = Twist()
    min_scan = min(min_scan)
    print("minimum back ", min_scan)
    if min_scan < 0.40:
        twist.linear.x = 0.2
        pub.publish(twist)
        print(twist)
        
        if min_scan > 0.35:
            rospy.sleep(1)
            twist.linear.x = 0.0
            pub.publish(twist)
    
def main():
    rospy.Subscriber("/base_scan",LaserScan,Scan)
    rospy.Subscriber("/base_scan_back",LaserScan,Scan_back)
    rospy.sleep(1)
    
    
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Laserscanner',anonymous=True)
    main()