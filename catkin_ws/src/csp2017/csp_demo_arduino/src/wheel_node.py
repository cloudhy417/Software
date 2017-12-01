#!/usr/bin/env python
import rospy
import numpy as np
from duckietown_msgs.msg import BoolStamped, Twist2DStamped

class arduinoWheel(object):
    def __init__(self):
        # =========== publisher ===========
        self.pub_car = rospy.Publisher("~car_cmd", Twist2DStamped, queue_size=1)
        # publish to topic "car_cmd" (you may have to see the code last week)

        # =========== subscriber ===========
        # subscribe to topic "result" (you should see arduino_node.py)

        self.sub_result = rospy.Subscriber("~result", BoolStamped, self.cbResult)
   # =========== subscribe distance from arduino ===========
    def cbResult(self, msg):
        cmd = Twist2DStamped()
        if not msg.data:
            cmd.v=0.2
            cmd.omega=0
            print "go forward"

        else:
            cmd.v=-0.2
            cmd.omega=0
            print "go backward"
        self.pub_car.publish(cmd)
if __name__ == "__main__":
    rospy.init_node("arduino_wheel", anonymous = False)
    arduino_node = arduinoWheel()
    rospy.spin()
