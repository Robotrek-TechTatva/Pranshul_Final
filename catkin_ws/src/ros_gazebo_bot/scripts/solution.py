#!/usr/bin/python3
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
from geometry_msgs.msg import Twist
def listener():
    rospy.init_node('listener',anonymous=True)
    while True:
        rospy.Subscriber("/a/depth/points",PointCloud2,call1)

def call1(data):
    data_out = pc2.read_points(data, skip_nans=True)
    data_out = list(data_out)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 0.1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
 
    if(min(data_out)[1] > 0.4):
        vel_msg.linear.x = 0.1
        vel_msg.linear.y = 1
    else:
        vel_msg.linear.y = 0
    velocity_publisher.publish(vel_msg)
        
listener()
