import os

tessim_path = os.environ['TESSIM_PATH']
import sys
sys.path.insert(0, tessim_path)

import cli_commands as cli
from matplotlib import pyplot as plt

atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'compiled/negative.hex', 1000000)
nodes = cli.createNodes(100)
atmega.connectNodes(nodes)
atmega.initCPULogFile(b'logs/atmega_cpu_logs.txt')
cli.putValue(96,2)
cli.putValue(9,5)
cli.putValue(60,5)
cli.putValue(97,5)

cli.execAll(0.00000025, 0.3)