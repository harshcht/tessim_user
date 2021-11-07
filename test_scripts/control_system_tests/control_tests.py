import sys
sys.path.insert(0, '../tessim')


import cli_commands as cli
from matplotlib import pyplot as plt
class rLC : 
    L = 0
    C = 0
    r = 0
    Vin = 0
    Vo = 0
    i=0
    t_pre = 0
    duty = 0
    v_on = 0
    v_off = 0
    pwm_src = 0
    node_in = 0
    node_out = 0
    def __init__(self,l,c,r, in_node, out_node):
        self.L = l
        self.C = c
        self.r = r
        self.node_in = in_node
        self.node_out = out_node
        cli.parts.append(self)

    def Exec(self, time) :
        self.Vin = cli.getNodeValue(self.node_in)
        dt = time - self.t_pre
        i_cache = self.i
        self.i = self.i + (self.Vin - self.Vo - self.r * self.i) * dt / self.L 
        self.Vo = self.Vo + i_cache * dt / self.C
        self.t_pre = time
        cli.putValue(self.node_out, self.Vo)
atmega = cli.mcu(cli.architecture_family.avr, cli.avr_mcu.atmega2560, b'/home/harsh/tessim_app/tessim/test_scripts/control_system_tests/compiled/control_tests.hex', 10000000)
#avr-objcopy -O ihex compiled/two_motor.elf compiled/two_motor_test.hex
#/opt/microchip/xc8/v2.32/bin/xc8-cc -mcpu=atmega2560 -O -o compiled/two_motor.elf two_motor.c 

nodes = cli.createNodes(100)
converter  = rLC(0.01, 0.005, 1, 24, 96)
cli.putValue(9, 10)
cli.putValue(60, 10)
#cli.putValue(96, 0)
atmega.connectNodes(nodes)
#cli.putValue(24 ,10)
atmega.initCPULogFile(b'logs/control_log.txt')
cli.putValue(97,10)
print("dirst half")
#cli.putValue(96, 4.5)
cli.execAll(0.000001, 0.5)
plt.plot(cli.simulation_time, cli.recorded_nodes[24])
plt.plot(cli.simulation_time, cli.recorded_nodes[96])
print(cli.recorded_nodes[96])
plt.show()



