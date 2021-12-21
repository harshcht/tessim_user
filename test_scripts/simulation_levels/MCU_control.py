from os import write
import sys
sys.path.insert(0, '/home/harsh/tessim_app/tessim')

import cli_commands as cli
from matplotlib import pyplot as plt
import csv
import numpy as np
import control

nodes = cli.createNodes(110)
Kt = 0.0255
Kb = 0.0255
Ra = 40.4
La = 0.00077
Jm = 0.0000013
Bm = 0.0000029374

time = np.linspace(0,1.5 , 5000)
Km = Kt/(Kt*Kb + Ra*Bm)
tm = Jm * Ra / (Kt*Kb + Ra*Bm)
ki = 0.5
s = control.tf([1,0],[1])
G = control.tf([Km],[tm,1])
H = ki/s
ref = 50
ref_tf = ref/s
mt = cli.dcMotor(0.0255,0.0255 , 40.4, 0.00077, 0.0000013, 0.0000029374)
mt.setSpeedNode(100)
mt.setNodes(102, 103)

driver1 = cli.real_motor_driver(0.000004,0.000008,0.000003,0.000003,2.5,2.5)
#driver1  = cli.generic_motor_drivers(2.5, 2.5)
driver1.connectNodes(101, 24, 102, 104)
encoder = cli.encoder(500, 100, 7, 8, 0.5, 0.2)
atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'compiled/exp_1_closed_loop.hex', 10000000)

atmega.connectNodes(nodes)
cli.putValue(9, 10)
cli.putValue(60, 10)
cli.putValue(101, 20)
cli.putValue(108, 50)

atmega.initCPULogFile(b'logs/encoder_logs.txt')
atmega.setCPUStatusLogs(b'logs/cpu_status.txt')
#mt.torque = 0.0003
cli.execAll(0.0000001, 1.5)
t,y = control.step_response(ref * control.feedback(H*G), time)
#plt.plot(cli.simulation_time, cli.recorded_nodes[7])
#plt.plot(cli.simulation_time, cli.recorded_nodes[24])
#plt.plot(cli.simulation_time, cli.recorded_nodes[23])
#plt.plot(cli.simulation_time, cli.recorded_nodes[102])
plt.plot(cli.simulation_time, cli.recorded_nodes[100], label = "speed from mcu")

plt.plot(t,y, label = "transfer function sim")

plt.xlabel("time (s)")
plt.ylabel("speed (rad/s)")
plt.legend()
top = ['time', 'speed', "volt at t1", "volt at t2", "input PWM1", "input PWM2"]
rows = [[cli.simulation_time[i], cli.recorded_nodes[100][i], cli.recorded_nodes[102][i], cli.recorded_nodes[103][i], cli.recorded_nodes[23][i], cli.recorded_nodes[24][i]] for i in range(len(cli.simulation_time))]
#plt.plot(cli.simulation_time, mt.speeds)
with open('record.csv', 'w') as record:
    write = csv.writer(record)
    write.writerow(top)
    write.writerows(rows)
plt.show()