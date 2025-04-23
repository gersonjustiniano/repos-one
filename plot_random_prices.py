import matplotlib.pyplot as plt
import numpy as np
import random

var={'time':[],'close':[]}

for i in range(100):
	var['time'].append(str(i+1))
	if len(var['close'])==0:
		var['close'].append(random.uniform(1,2))
	else:
		up=var['close'][-1]*(1+0.01)
		down=var['close'][-1]*(1-0.01)
		var['close'].append(random.uniform(down,up))
	print(len(var['time']),var['time'][-1],var['close'][-1])

fig=plt.figure()
ax=fig.add_subplot()

ax.clear()
ax.set_xticks([])
ax.plot(var['time'],var['close'],c='black',lw=1)

plt.show()
