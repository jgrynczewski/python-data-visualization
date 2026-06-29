import random

# import matplotlib
# matplotlib.use('WebAgg')
from matplotlib import pyplot as plt
import numpy as np

# print(matplotlib.get_backend())
# print(matplotlib.rcsetup.backend_registry.list_all())

# Wykres sinusa z szumem
x1 = [x*0.01 for x in range(0, 628)]
y1 = [np.sin(x*0.01) + random.gauss(0, 0.1) for x in range(0, 628)]
plt.plot(x1, y1)

# Wykres cosinusa+ random.gauss(0, 0.1)
x2 = [x*0.5 for x in range(0, round(63/5))]
y2 = [np.cos(x*0.5) for x in range(0, round(63/5))]
plt.plot(x2, y2, 'o-')

plt.show()
