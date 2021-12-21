import sys
sys.path.insert(0,'/home/harsh/tessim_app/tessim')

import numpy as np
import cli_commands as cli
from matplotlib import pyplot as plt
import math
import control
import csv

Kt = 0.0255
Kb = 0.0255
Ra = 40.4
La = 0.00077
Jm = 0.0000013
Bm = 0.0000029374

time = np.linspace(0,2 , 5000)
Km = Kt/(Kt*Kb + Ra*Bm)
tm = Jm * Ra / (Kt*Kb + Ra*Bm)
Cm = Ra / (Kt*Kb + Ra*Bm)
ki = 1600
s = control.tf([1,0],[1])
G = control.tf([Km],[tm,1])
H = ki/s
G1 = control.tf([Kt],[Jm*La, Jm*Ra + Bm*La, Kt*Kb + Bm*Ra])
#print(G1)
t,y = control.step_response(control.feedback(H*G), time)
t,y1 = control.step_response(control.feedback(H*G1), time)
top = ['time','speed(first order)', 'speed(second order)']
rows = [[t[i],y[i], y1[i]] for i in range(len(t))]
with open('record.csv','w') as record:
    write = csv.writer(record)
    write.writerow(top)
    write.writerows(rows)
plt.xlabel("time (s)")
plt.ylabel("Responose")
plt.plot(t,y)
#plt.ylim(0, 15)
plt.show()