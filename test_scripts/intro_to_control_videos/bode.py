import control
import numpy as np
import matplotlib.pyplot as plt
Kt = 0.0255
Kb = 0.0255
Ra = 40.4
La = 0.00077
Jm = 0.0000013
Bm = 0.0000029374

time = np.linspace(0,1.5 , 5000)
Km = Kt/(Kt*Kb + Ra*Bm)
tm = Jm * Ra / (Kt*Kb + Ra*Bm)
wo = 1/tm
freq_range = np.logspace(-5, 5, 100000)
G = control.tf([Km],[tm,1])
print(wo)
control.bode_plot(G,freq_range)
plt.show()