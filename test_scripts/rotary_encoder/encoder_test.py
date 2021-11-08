import os

tessim_path = os.environ['TESSIM_PATH']
import sys
sys.path.insert(0, tessim_path)

import cli_commands as cli
from matplotlib import pyplot as plt

cli.createNodes(4)

encoder = cli.encoder(10, 0, 1, 2, 0.5, 0.2)
cli.putValue(0, 1)

cli.execAll(0.0001, 10)

plt.plot(cli.simulation_time, cli.recorded_nodes[1])
plt.plot(cli.simulation_time, cli.recorded_nodes[2])
plt.show()

