from os import write
import os
tessim_path = os.environ['TESSIM_PATH']
import sys
sys.path.insert(0, tessim_path)

import cli_commands as cli
from matplotlib import pyplot as plt
import csv

nodes = cli.createNodes(110)

mt = cli.dcMotor(0.0255,0.0255 , 40.4, 0.00077, 0.0000013, 0.0000029374)
mt.setSpeedNode(100)
mt.setNodes(102, 103)

mt2 = cli.dcMotor(0.0255,0.0255 , 40.4, 0.00077, 0.0000013, 0.0000029374)
mt2.setNodes(105, 106)
mt2.setSpeedNode(107)
cli.putValue(105, 10)
driver1  = cli.generic_motor_drivers(2.5, 2.5)
driver2  = cli.generic_motor_drivers(2.5, 2.5)
driver1.connectNodes(101, 24, 102, 104)
driver2.connectNodes(101, 23, 103, 104)
encoder = cli.encoder(500, 100, 7, 8, 0.5, 0.2)
atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'compiled/open_loop.hex', 10000000)

atmega.connectNodes(nodes)
cli.putValue(9, 10)
cli.putValue(60, 10)
cli.putValue(101, 20)
cli.putValue(108, 50)

atmega.initCPULogFile(b'logs/encoder_logs.txt')
atmega.setCPUStatusLogs(b'logs/cpu_status.txt')
mt.torque = 0.0003
cli.execAll(0.000001, 1)

plt.plot(cli.simulation_time, cli.recorded_nodes[7])
#plt.plot(cli.simulation_time, cli.recorded_nodes[24])
#plt.plot(cli.simulation_time, cli.recorded_nodes[23])
#plt.plot(cli.simulation_time, cli.recorded_nodes[102])
plt.plot(cli.simulation_time, cli.recorded_nodes[100], label = "speed from mcu")
plt.plot(cli.simulation_time, cli.recorded_nodes[107], label="expected response")
#plt.plot(cli.simulation_time, cli.recorded_nodes[105])
plt.xlabel("time (s)")
plt.ylabel("speed (rad/s)")
plt.legend()
top = ['time', 'speed', "volt at t1", "volt at t2"]
rows = [[cli.simulation_time[i], cli.recorded_nodes[100][i], cli.recorded_nodes[9][i], cli.recorded_nodes[107][i]] for i in range(len(cli.simulation_time))]
#plt.plot(cli.simulation_time, mt.speeds)
with open('record.csv', 'w') as record:
    write = csv.writer(record)
    write.writerow(top)
    write.writerows(rows)
plt.show()

