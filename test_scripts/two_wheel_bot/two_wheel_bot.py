import os

tessim_path = os.environ['TESSIM_PATH']
import sys
sys.path.insert(0, tessim_path)

import cli_commands as cli
from matplotlib import pyplot as plt
import math
import ctypes
from ctypes import c_char_p, c_double, c_void_p, cdll

x1 = []
x2 = []
y1 = []
y2 = []
xcm = []
ycm = []

class robot  :
    r1 = 1
    r2 = 1 #radius of botht he motors
    speed1 = 0
    speed2  = 0
    robot_linear_speed = 0
    robot_angular_speed = 0
    speed_pre = 0
    theta = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    width = 0
    xcm = 0
    ycm = 0
    time_pre = 0
    motor_obj1 = None
    motor_obj2 = None
    def __init__(self, r1, r2, width) :
        self.r1 = r1
        self.r2 = r2
        self.width = width
        self.x2 = width
        self.xcm = width / 2
        cli.parts.append(self)
        self.motor_obj1 = cli.dcMotor(0.05,0.05 , 0.5, 0.0015, 0.00025, 0.001)
        self.motor_obj2 = cli.dcMotor(0.05,0.05 , 0.5, 0.0015, 0.00025, 0.001)
        self.motor_obj1.setNodes(101,102)
        self.motor_obj2.setNodes(103,104)
    
    def Exec(self, time):
        #self.motor_obj.Exec(time)
        self.speed1 = self.r1 * self.motor_obj1.getSpeed()
        self.speed2 = self.r2 * self.motor_obj2.getSpeed()
        self.theta += (self.speed2 - self.speed1) * (time - self.time_pre) / self.width
        vcm  = (self.speed1 + self.speed2) / 2
        vy  = vcm * math.cos(self.theta)
        vx  = -vcm * math.sin(self.theta)
        self.xcm += vx * (time - self.time_pre)
        self.ycm += vy * (time - self.time_pre)
        self.x2 = self.xcm + self.width * math.cos(self.theta) / 2
        self.x1 = self.xcm - self.width * math.cos(self.theta) / 2
        self.y2 = self.ycm + self.width * math.sin(self.theta) / 2
        self.y1 = self.ycm - self.width * math.sin(self.theta) / 2
        self.time_pre = time
        x1.append(self.x1)
        x2.append(self.x2)
        y1.append(self.y1)
        y2.append(self.y2)
        xcm.append(self.xcm)
        ycm.append(self.ycm)
        self.speed_pre = self.speed1

    def assignMtPtr(self, mtr_ptr):
        self.motor_obj = mtr_ptr



nodes = cli.createNodes(110)

atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'compiled/two_motor_test.hex', 1000000)
driver1  = cli.generic_motor_drivers(2.5, 2.5)
driver2  = cli.generic_motor_drivers(2.5, 2.5)
driver3  = cli.generic_motor_drivers(2.5, 2.5)
driver4  = cli.generic_motor_drivers(2.5, 2.5)
driver1.connectNodes(100,24,101,10)
driver2.connectNodes(100,23,102,10)
driver3.connectNodes(100,4,104,10)
driver4.connectNodes(100,5,103,10)
cli.putValue(97, 5)
cli.putValue(9, 5)
cli.putValue(60, 5)
cli.putValue(100, 12)
cli.putValue(18, 5)
atmega.connectNodes(nodes)
rb = robot(0.05, 0.05, 0.2)
cli.execAll(0.0000025, 0.6)
cli.putValue(18,0)

#cli.putValue(20,5)
cli.execAll(0.0000025, 0.3)
cli.putValue(20,5)
cli.execAll(0.0000025, 0.1)
cli.putValue(20,0)
cli.execAll(0.0000025, 0.2)
cli.putValue(18,5)
cli.execAll(0.0000025, 0.3)
#plt.plot(cli.simulation_time, cli.recorded_nodes[24])
#plt.plot(cli.simulation_time, cli.recorded_nodes[5])
#plt.show()

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(xcm, ycm)
plt.legend(["left motor", "right motor", "center"])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


plt.plot(cli.simulation_time, rb.motor_obj1.speeds)
plt.plot(cli.simulation_time, rb.motor_obj2.speeds)
plt.legend(["speed : left motor", "speed : right motor"])
plt.xlabel("time")
plt.ylabel("speed (rad/s)")
plt.show()



        
