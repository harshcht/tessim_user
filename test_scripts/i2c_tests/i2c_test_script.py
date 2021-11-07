import os

tessim_path = os.environ['TESSIM_PATH']
import sys
sys.path.insert(0, tessim_path)
import cli_commands as cli
from matplotlib import pyplot as plt
#SCENARIIO_1 : mcu as slave debugger as master : Send slave address and then send data

#case 1: ack of master is enabledmega
atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'compiled/avr_scenario_1.hex', 1000000)
atmega2 = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'compiled/avr_scenario_2.hex', 1000000)
#print("instance created")
#atmega.setTwiLog(b'logs/atmega_twi_logs.txt')
atmega2.setTwiLog(b'logs/atmega2_twi.txt')
atmega.initCPULogFile(b'logs/atmega_cpu_logs.txt')
atmega2.initCPULogFile(b'logs/atmega2_cpu_logs.txt')
nodes = cli.createNodes(200)
atmega2.setTWILine(atmega.getTWILine())
atmega2.setTWIDebuggerLogs(b'logs/atmega2_twi_dbgr_logs.txt')
atmega.setTWIDebuggerLogs(b'logs/atmega_twi_dbgr_logs.txt')
atmega2.setTWIClock(atmega.getTWIClock())
###mt.setNodes(14,  0)
atmega.connectNodes(nodes)
atmega2.connectNodes(nodes + 100)
cli.putValue(97, 5)
cli.putValue(9, 5)

cli.putValue(96, 2)
#print("ndes formed")
#dbgr = cli.TWI_debugger(1, cli.debugger_type.slave_twi, atmega.getTWIClock(), b'logs/debugger_logs.txt')
##print("debugger formed")
#dbgr.setState(cli.twi_state.twi_idle)
#dbgr.enableGeneralCallAck(True)
#dbgr.enableAck(True)
##line  = cli.TWI_line(0)
##print("line created")
##line.addSDAPtr(dbgr.getSDAPtr())
##
##print("added sda pointer")
###line.setLineSDA( dbgr.getSDAPtr(), 0)
#dbgr.connectLine(atmega.getTWILine())
##print("line connected")
#dbgr.setSDA(0x8F)
##print("sda written")
cli.execAll(0.00000025, 0.000018)
##dbgr.setState(cli.twi_state.twi_send_start)
cli.execAll(0.00000025, 0.001)
##dbgr.setState(cli.twi_state.twi_send_start)
cli.execAll(0.00000025, 0.001)