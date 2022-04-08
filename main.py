import matplotlib.pyplot as plt
import numpy as np

data = np.transpose(np.loadtxt('cmake-build-debug/write.txt'))
x = np.arange(1, len(data[0]) + 1)
plt.plot(x, data[0])
plt.grid()
plt.show()
