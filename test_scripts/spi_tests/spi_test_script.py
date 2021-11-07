import os

tessim_path = os.environ['TESSIM_PATH']
import sys
sys.path.insert(0, tessim_path)

import cli_commands as cli
from matplotlib import pyplot as plt

clk = cli.Clock(0.00001, 0.5, cli.clock_types.oscillator)
a = b'\x8f'
dbgr_master  = cli.SPI_debugger(1, cli.debugger_type.master_spi, clk.clock_obj)
dbgr_master.setOutputReg(a)
atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'compiled/spi_test.hex', 1000000)
atmega.initCPULogFile(b'logs/atmega_cpu_logs.txt')
atmega.setSPILogs(b'logs/spi_logs.txt')
nodes = cli.createNodes(100)
atmega.connectNodes(nodes)
dbgr_master.connectNodes(21,20,18)
clk.connectNode(19)
cli.putValue(9,5)
cli.putValue(60,5)
cli.putValue(20, 5)
cli.execAll(0.000000025, 0.0001)

plt.plot(cli.recorded_nodes[19])
plt.plot(cli.recorded_nodes[20])
plt.plot(cli.recorded_nodes[21])
plt.show()

#debugger tests 
#clk = cli.Clock(0.000001, 0.5, cli.clock_types.oscillator)
#dbgr_master  = cli.SPI_debugger(1, cli.debugger_type.master_spi, clk.clock_obj)
#a = b'\x8f'
#dbgr_master.setOutputReg(a)
#nodes = cli.createNodes(4)
#clk.connectNode(3)
#dbgr_master.connectNodes(0,1,2)
#dbgr_slave =  cli.SPI_debugger(1, cli.debugger_type.master_spi, clk)
#print("executing now")
#cli.execAll(0.000000025, 0.00001)

#plt.plot(cli.recorded_nodes[1])
#plt.plot(cli.recorded_nodes[3])
#plt.show()