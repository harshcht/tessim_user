import sys
sys.path.insert(0, '/home/harsh/tessim_app/tessim')

import python_cli_commands as cli
from matplotlib import pyplot as plt

mt = cli.dcMotor(0.05,0.05 , 0.5, 0.0015, 0.00025, 0.001)
#Normal motor test
nodes = cli.createNodes(2)
mt.setNodes(0,1)
#cli.putValue(0,10)
src = cli.sine_source(5,0)
cli.execAll(0.0000025, 6)
plt.plot(mt.time, mt.speeds)
plt.xlabel("time (s)")
plt.ylabel("speed (rad/s)")
plt.show()

cli.reset()

#atmega controller with a compiled hex file as program
#syntax : mcu(num_pins, architecture_family, part_num)
atmega = cli.mcu(32, cli.architecture_family.avr, cli.avr_mcu.atmega328p, b'compiled/single_motor_control.hex')


#motor drivers with low and high thresholds
#syntax : generic_motor_driver(low_th, high_th)
#low_th : driver output is zero if input signal level is bellow this value
#high_th : driver outputs high(VCC) if input level is above this value
driver1  = cli.generic_motor_drivers(2.5, 2.5)
driver2  = cli.generic_motor_drivers(2.5, 2.5)

#a motor
#syntax : dcMotor(kt, ke, r, l, jm, bm)
#kt  torque constant
#ke electrical constant
#r : armature resistance
#l : motor inductance
#jm : motor inertia
#bm : friction coefficient. 
mt = cli.dcMotor(0.05,0.05 , 0.5, 0.0015, 0.00025, 0.001)


#create a total of 36 nodes are needed for the system (32 are directly connected to the mcu)
nodes = cli.createNodes(36)

#the drivers are connedted as follows :
#   connectNodes(Vcc, vin, Vout, gnd)
#   In this example node 32 proivides 15v VCC to both the drivers
#   Input signal to driver 1 and driver 2 is given by pin 10 and 9 of th controller respectively
#   (which are OC0A and OC0B pins respectively) 
#   Output of each driver is connected to node 34 and 33 which are connected to the motor
driver1.connectNodes(32,9,34,35)
driver2.connectNodes(32, 8, 33, 35)

#connect motor to the output of the driver
mt.setNodes(34,  33)

#nodes 0 to 31 (first 32 nodes) will be connected to the 
#32 pins of the controller
atmega.connectNodes(nodes)
#nodes are numberd from 0 to 35. The first 32 ndes will be conncted to the mcu. 
#Thus node 0 is connected to pin 1 of mcu node 1 to pin 2 and so on
cli.putValue(32, 15) #15v power supply to drivers
cli.putValue(35, 0) #ground pin of motor drivers
cli.putValue(3,5) #5v power supply to the micro-controller
cli.putValue(11, 5) #node 11 is pin 12, to 
                    #which the buitton is attatched
                    # giving a value of 5v means that the button is pressed

#executing all the components : 
#syntax : execAll(time_div, time
# #time_div : time division for simulation
# #tims : total length of time for simulation
cli.execAll(0.00000025, 0.5)
print("speed with button pressed : ", mt.getSpeed())
cli.putValue(11,0) #button is released
cli.execAll(0.00000025, 0.5)
print("speed with button released : ", mt.getSpeed())
cli.putValue(11, 5) #pressed again
cli.execAll(0.00000025, 0.5)
plt.plot(mt.time, mt.speeds)
plt.xlabel("time (s)")
plt.ylabel("speed (rad/s)")
plt.show()
print(mt.getSpeed())