import sys
sys.path.insert(0, '/home/harsh/tessim_app/tessim')

import cli_commands as cli

atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'/home/harsh/tessim_app/tessim/test_scripts/mppt_controller/compiled/mppt_test.hex', 1000000)
nodes = cli.createNodes(100)
atmega.connectNodes(nodes)
cli.putValue(9, 5)
cli.putValue(60, 5)
cli.putValue(97, 5)
cli.putValue(96,3.5)

cli.execAll(0.000000025, 0.05)
