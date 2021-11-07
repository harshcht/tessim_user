import sys
sys.path.insert(0, '../')

import cli_commands as cli
from matplotlib import pyplot as plt






#cli.reset()


#atmega controller with a compiled hex file as program
#syntax : mcu(num_pins, architecture_family, part_num)
#atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'compiled/pwm_test.hex', 1000000)

#motor drivers with low and high thresholds
#syntax : generic_motor_driver(low_th, high_th)
#low_th : driver output is zero if input signal level is bellow this value
#high_th : driver outputs high(VCC) if input level is above this value
#driver1  = cli.generic_motor_drivers(2.5, 2.5)
#driver2  = cli.generic_motor_drivers(2.5, 2.5)

#a motor
#syntax : dcMotor(kt, ke, r, l, jm, bm)
#kt  torque constant
#ke electrical constant
#r : armature resistance
#l : motor inductance
#jm : motor inertia
#bm : friction coefficient. 
#mt = cli.dcMotor(0.05,0.05 , 0.5, 0.0015, 0.00025, 0.001)


#create a total of 36 nodes are needed for the system (100 are directly connected to the mcu)
#nodes = cli.createNodes(104)

#the drivers are connedted as follows :
#   connectNodes(Vcc, vin, Vout, gnd)
#   In this example node 100 proivides 15v VCC to both the drivers
#   Input signal to driver 1 and driver 2 is given by pin 25 and 24 of th controller respectively
#   (which are OC0A and OC0B pins respectively) 
#   Output of each driver is connected to node 102 and 103 which are connected to the motor
#driver1.connectNodes(100,24,101,10)
#driver2.connectNodes(100,23,102,10)

#connect motor to the output of the driver
#mt.setNodes(101,102)
#atmega.connectNodes(nodes)
#cli.putValue(97, 5)
#cli.putValue(9, 5)
#cli.putValue(100, 12)


#cli.putValue(18, 5) #node 18 is pin 19, to 
                    #which the buitton is attatched
                    # giving a value of 5v means that the button is pressed

#executing all the components : 
#syntax : execAll(time_div, time
# #time_div : time division for simulation
# #tims : total length of time for simulation
#cli.execAll(0.0000025, 0.5)
#print("speed with button pressed : ", mt.getSpeed())
#cli.putValue(18,0) #button is released
#cli.execAll(0.0000025, 0.5)
#print("speed with button released : ", mt.getSpeed())
#cli.putValue(18, 5) #pressed again
##cli.execAll(0.0000025, 0.5)
#plt.plot(mt.time, mt.speeds)
#plt.xlabel("time (s)")
#plt.ylabel("speed (rad/s)")
#plt.show()


#cli.reset()

atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'/home/harsh/tessim_demo/compiled/adc_test.hex', 1000000)
driver1  = cli.generic_motor_drivers(2.5, 2.5)
driver2  = cli.generic_motor_drivers(2.5, 2.5)
mt = cli.dcMotor(0.05,0.05 , 0.5, 0.0015, 0.00025, 0.001)


nodes = cli.createNodes(104)
driver1.connectNodes(100,24,101,10)
driver2.connectNodes(100,23,102,10)
mt.setNodes(101,102)
atmega.connectNodes(nodes)
#sinusoidal source 
#syntax : sine_source(freq, node, offset, amplitude)
src = cli.sine_source(50,96, 2, 2.5)
#cli.putValue(96, 0.5)
cli.putValue(97, 5)
cli.putValue(9, 5)
cli.putValue(60, 5)
cli.putValue(20,5)
cli.putValue(22, 5)
cli.putValue(100, 12)
cli.execAll(0.000025, 1)

plt.plot(mt.time, mt.speeds)
plt.plot(mt.time[0:1001], cli.recorded_nodes[96][0:1001])
#plt.plot(mt.time, cli.recorded_nodes[102])
#plt.plot(mt.time, cli.recorded_nodes[23])
#plt.plot(mt.time, cli.recorded_nodes[24])
plt.plot(mt.time[0:1001],cli.recorded_nodes[101][0:1001])
plt.xlabel("time (s)")
plt.ylabel("speed (rad/s)")
plt.show()
print(mt.getSpeed())

cli.reset()

