import sys
import os
from matplotlib import pyplot as plt


tessim_path = os.environ['TESSIM_PATH']
sys.path.insert(0, tessim_path)

import cli_commands as cli
cli.createNodes(6)
mt = cli.dcMotor(0.0255,0.0255 , 40.4, 0.00077, 0.0000013, 0.0000029374)
mt.setNodes(0,1)
mt.torque = 0.0003

cli.putValue(0, 10)

mt.setSpeedNode(2)


encoder = cli.encoder(500, 3, 4,5, 0.5, 0.2)
cli.putValue(3, 200)
cli.execAll(0.0001, 0.2)

plt.plot(cli.simulation_time, cli.recorded_nodes[4])
plt.plot(cli.simulation_time, cli.recorded_nodes[5])
plt.show()