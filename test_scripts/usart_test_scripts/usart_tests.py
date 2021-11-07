import sys
sys.path.insert(0, '/home/harsh/tessim_app/tessim')
import cli_commands as cli
from matplotlib import pyplot as plt

#clk = cli.Clock(0.01, 0.5, cli.clock_types.oscillator)
#debugger = cli.uart_debugger(2, clk.clock_obj)
atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'compiled/usart_test.hex', 1000000)
nodes = cli.createNodes(100)
atmega.connectNodes(nodes)
atmega.initCPULogFile(b'logs/cpu_logs.txt')
cli.putValue(9,5)
cli.putValue(60,5)
cli.putValue(20, 5)
cli.execAll(0.000000025, 0.0001)
#clk.connectNode(0)
#debugger.setTicks(cli.clock_ticks.low_to_high, cli.clock_ticks.high_to_low)
#debugger.setSynch(True)
#debugger.enableTxRx(True, True)
#debugger.connect(1,2)
#data = b'\x8f\x8e'
##debugger.setOutputBuff(data)
#debugger.setState(cli.usart_tx_state.usart_tx_start)
#debugger.setParity(cli.t_parity.odd_parity)
#debugger.txSettings(9,cli.t_parity.even_parity,2)
#debugger.setBits(9)
#cli.putValue(1, 0)

#cli.execAll(0.0001, 0.3)

plt.plot(cli.simulation_time, cli.recorded_nodes[2])
plt.plot(cli.simulation_time, [1.5 * x for x in cli.recorded_nodes[3]] )
plt.show()