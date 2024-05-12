#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import JointState

class Mynode(Node):
    def __init__(self):
        super().__init__("rviz_to_gazebo")
        self.get_logger().info("Rviz to Gazebo started")
        self.cmd_vel_pub_=self.create_publisher(Float64MultiArray,"/hexapod_controller/commands",10)
        self.timer=self.create_timer(0.5,self.send_value)
    
    def send_value(self):
        msg = Float64MultiArray()
        self.joint_input=int(input("Joint to move: "))
        self.joint_value=float(input("Value for the joint: "))
        msg.data=[0.0] * 18 
        msg.data[self.joint_input-1]=self.joint_value 
        self.cmd_vel_pub_.publish(msg)
        self.get_logger().info('Publishing: %s' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    node=Mynode()
    
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=='__main__':
    main()
