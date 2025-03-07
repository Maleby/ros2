#!/usr/bin/env python

import rclpy
from rclpy.node import Node
import random

class TemperatureNode(Node):
    def __init__(self,timer_period=0.2):
        # call super() in the constructor to initialize the Node object
        # the parameter we pass is the node name
        
        super().__init__('temperature_monitor')
        self.get_logger().info('Temperature Monitor Node has been started.')
        self.temperature_threshold = 70.0
        self.create_timer(timer_period, self.timer_callback)

    def get_temperature(self):
        # Simulate getting a temperature reading (in reality, this would come from a sensor)
        temperature = random.uniform(20.0, 100.0)
        return temperature




    def timer_callback(self):
        current_temperature = self.get_temperature()
        if current_temperature < self.temperature_threshold:
            self.get_logger().info(f'Current temperature: {current_temperature:.2f}°C')
        else: 
            self.get_logger().warn(f'Warning: High temperature detected! {current_temperature:.2f}°C')
        

def start_monitor(args=None):
    # initialize the ROS2 communication
    rclpy.init(args=args)
    # declare the node constructor
    node = TemperatureNode(timer_period=1.0)
    # keeps the node alive, waits for a request to kill the node (ctrl+c)
    try:
        rclpy.spin(node)  # Keep the node running, processing callbacks
    except KeyboardInterrupt:
        pass
    # shutdown the ROS2 communication
    rclpy.shutdown()



if __name__ == '__main__':
    start_monitor()