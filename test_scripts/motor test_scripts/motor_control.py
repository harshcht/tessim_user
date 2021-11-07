import os

tessim_path = os.environ['TESSIM_PATH']
import sys
sys.path.insert(0, tessim_path)

import cli_commands as cli
from matplotlib import pyplot as plt

#create motor with the following partameters 
#a motor
#syntax : dcMotor(kt, ke, r, l, jm, bm)
#kt  torque constant
#ke electrical constant
#r : armature resistance
#l : motor inductance
#jm : motor inertia
#bm : friction coefficient.
#all values are in SI units
mt = cli.dcMotor(0.05,0.05 , 0.5, 0.0015, 0.00025, 0.001)

#Normal motor test
nodes = cli.createNodes(2)

#assign nodes to the motor (v+, v-)
mt.setNodes(1, 0)

#cli.putValue(1, 10) #incput voltage
clk = cli.Clock(0.001, 0.2, cli.clock_types.oscillator)
clk.connectNode(1)
#simulate for 0.2 sec with a time divisio of 25us
cli.execAll(0.000025, 0.2)

#plot the speed as a function of time
plt.plot(cli.simulation_time, mt.speeds)
#plt.plot(cli.simulation_time, cli.recorded_nodes[1])
plt.xlabel("time (s)")
plt.ylabel("speed (rad/s)")
plt.show()

#mt.setSpeedNode(2)
#cli.putValue(0,10)
#cli.putValue(3, 100)
#src = cli.sine_source(5,0)
#adder = cli.Adder(2, 3, 4)
#integrator = cli.Integrator(2, 4)
#integrator.assignOutputNode(0)
#adder.setNegative(True, False, False)
cli.reset()

#nodes = cli.createNodes(2)
#integrator = cli.Integrator(1, nodes + 0)
#src= cli.sine_source(5, 0,1,0.1)
#integrator.assignOutputNode(1)
#cli.execAll(0.01, 6)
#plt.plot(cli.simulation_time,cli.recorded_nodes[0])
#plt.plot(cli.simulation_time, cli.recorded_nodes[1])
#plt.show()