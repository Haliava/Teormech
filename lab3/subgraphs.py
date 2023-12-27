import matplotlib.pyplot as plt
from constants import *

fig = plt.figure()
graph = fig.add_subplot(1, 1, 1)
graph.set_xlabel("t")
graph.set_ylabel("s(t)")
graph.plot(t, S_T)
plt.show()
