import sys
sys.path.insert(0, '/home/harsh/tessim_app/tessim')


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
offgrid_inverter.updateOutput.argtypes = [ctypes.c_double, ctypes.c_void_p]


nd_out = 2
nd_grid = 1
nd_in = 0
curr_node = 3

class controller :
    controller_obj = 0
    node_in = 0
    node_ref = 0
    node_out = 0
    def __init__(self, freq, nd_in, nd_out, nd_ref, sample_time):
        self.controller_obj = offgrid_inverter.createController(freq, sample_time)
        self.node_in = nd_in
        self.node_out = nd_out
        self.node_ref = nd_ref
        cli.parts.append(self)

    def Exec(self, time):
        vin = cli.getNodeValue(self.node_in)
        vref = cli.getNodeValue(self.node_ref)
        #offgrid_inverter.updateOutput(time, self.controller_obj)
        #state = offgrid_inverter.updatePWM(time, self.controller_obj)
        #print(state)
        offgrid_inverter.updateDuty(vin, vref, self.controller_obj, time)
        state = offgrid_inverter.updatePWM(time,self.controller_obj)
        if(state):
            cli.putValue(self.node_out, 40)
        else:
            cli.putValue(self.node_out, -40)

class LC_grid_tied :
    nd_in=0
    nd_out = 0
    nd_grid = 0
    i_in = 0
    i_out = 0
    L = 0
    C = 0
    r = 0
    Lgrid = 0
    t_pre = 0
    grid_current = []
    def __init__(self, l, c, r, lg, nd_in, nd_out, nd_grid) :
        self.L = l
        self.C = c
        self.r = r
        self.nd_in = nd_in
        self.nd_out = nd_out
        self.nd_grid = nd_grid
        self.Lgrid = lg
        cli.parts.append(self)

    def Exec(self, time):
        dt = time - self.t_pre
        Vin = cli.getNodeValue(self.nd_in)
        Vout = cli.getNodeValue(self.nd_out)
        Vgrid = cli.getNodeValue(self.nd_grid)
        i_cache = self.i_in
        self.i_in += (dt / self.L) * (Vin - Vout - self.r * self.i_in)
        self.i_out += (dt / self.Lgrid) * (Vgrid - Vout - self.i_in * self.r)
        Vout +=  (dt / self.C) * (i_cache - self.i_out)
        cli.putValue(self.nd_out, Vout)
        cli.putValue(curr_node, self.i_out)
        self.t_pre = time



nodes = cli.createNodes(4)
grid = cli.sine_source(2 * pi * 50, nd_grid, 40, 0)
converter = LC_grid_tied(0.001,0.00005,1, 0.1, nd_in, nd_out, nd_grid)
ctrl = controller(50, nd_out, nd_in, nd_grid, 0.0001)


cli.execAll(0.0000001, 15)

plt.plot(cli.simulation_time, cli.recorded_nodes[nd_grid])
plt.plot(cli.simulation_time, cli.recorded_nodes[nd_out])
plt.plot(cli.simulation_time, cli.recorded_nodes[curr_node])
plt.show()