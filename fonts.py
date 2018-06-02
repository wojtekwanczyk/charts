from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Verdana']
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3],[1, 2, 1], label='test')

ax.legend()
plt.show()