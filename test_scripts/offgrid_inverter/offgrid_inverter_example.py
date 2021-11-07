import os

tessim_path = os.environ['TESSIM_PATH']
import sys
sys.path.insert(0, tessim_path)

import cli_commands as cli
from matplotlib import pyplot as plt

import ctypes
from ctypes import c_char_p, c_double, c_void_p, cdll
import enum
import math

pi = 3.14159265
offgrid_inverter = cdll.LoadLibrary('build/libinverter.so')
offgrid_inverter.createController.argtypes = [ctypes.c_double, ctypes.c_double]
offgrid_inverter.createController.restype = ctypes.c_void_p
offgrid_inverter.updatePWM.argtypes = [ctypes.c_double, ctypes.c_void_p]
offgrid_inverter.updateDuty.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_void_p, ctypes.c_double]
offgrid_inverter.updateGridTiedDuty.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_void_p,ctypes.c_double]
class sine_pwm_controller :
    controller_obj = 0
    nd_in = 0
    nd_ref = 0
    nd_out = 0
    input_volt = []
    delay = 0.01
    def __init__(self, freq, node_in, node_ref, node_out, sample_time):
        self.controller_obj = offgrid_inverter.createController(freq, sample_time)
        cli.parts.append(self)
        self.nd_in = node_in
        self.nd_ref = node_ref
        self.nd_out = node_out

    def Exec(self, time):
        vin = cli.getNodeValue(self.nd_in)
        #self.input_volt.append(cli.getNodeValue(self.nd_in))
        vref = cli.getNodeValue(self.nd_ref)
        offgrid_inverter.updateDuty(vin, vref, self.controller_obj, time)
        #offgrid_inverter.updateGridtiedDuty(vin, vref, self.controller_obj, time)
        state = offgrid_inverter.updatePWM(time, self.controller_obj)

        if state:
            cli.putValue(self.nd_out, 50)

        else :
            cli.putValue(self.nd_out, -50)


class LC :
    L = 0
    C = 0
    i = 0
    v = 0
    r = 0
    t_pre = 0
    node_in = 0
    node_out = 0
    def __init__(self, l,c, node_in, node_out, r):
        self.L = l
        self.C = c
        self.node_in = node_in
        self.node_out = node_out
        self.r = r
        cli.parts.append(self)
        
    def Exec(self, time):
        dt = time - self.t_pre
        Vin = cli.getNodeValue(self.node_in)
        Vo = cli.getNodeValue(self.node_out)
        i_cache = self.i
        self.i = self.i + (Vin - Vo - self.r * self.i) * dt / self.L 
        Vo = Vo + i_cache * dt / self.C
        cli.putValue(self.node_out, Vo) 
        #print("dt : ", dt, "Vo : ", Vo, "time : ", time)
        self.t_pre = time

nodes  = cli.createNodes(5)
ref = cli.sine_source(2 * pi * 50 , 3, 40, 0)
pwm = sine_pwm_controller(50, 1,3,0, 0.0001)
#cli.putValue(3, 1)
#counter = cli.counter_pwm(8, 1, 2)
#counter.setMode(cli.counter_pwm_modes.up_only)
#counter.setToptoDefault()
#counter.setCounterClockFreq(100000)
#counter.setCounterCompare(0, 128)
#counter.setPWMVcc(10)
#cli.putValue(0,-5)
#clk = cli.Clock(0.00001, 0.5, cli.clock_types.oscillator)
#clk.connectNode(0)
lc = LC(0.001, 0.00005, 0, 1, 1)
cli.execAll(0.0000001, 10)

#plt.plot(cli.simulation_time, cli.recorded_nodes[0])
#plt.plot(cli.simulation_time,cli.recorded_nodes[1])
#plt.plot(cli.simulation_time, cli.recorded_nodes[0])
plt.plot(cli.simulation_time, cli.recorded_nodes[1])
plt.plot(cli.simulation_time, cli.recorded_nodes[3])
error  = [cli.recorded_nodes[3][i] - cli.recorded_nodes[1][i] for i in range(len(cli.recorded_nodes[0]))]
plt.plot(cli.simulation_time, error)
plt.show()