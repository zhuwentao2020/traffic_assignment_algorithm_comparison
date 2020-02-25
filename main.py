import matplotlib.pyplot as plt
import json
import msa
import classic
import numpy as np
import time

# 读取基础数据
with open('parameter.json', 'r') as load_f:
    p = json.load(load_f)

demand = np.array(p['demand'])
capacity = np.array(p['capacity'])
free = np.array(p['free'])
n = np.array(p['number'])

# 计算
start_time_msa = time.time()
x, ttime = msa.msa(demand, capacity, free, n)
end_time_msa = time.time()
time_msa = end_time_msa - start_time_msa
print(f'time_msa:{time_msa}')

start_time_classic = time.time()
x1, time1 = classic.classic(demand, capacity, free, n)
end_time_classic = time.time()
time_classic = end_time_classic - start_time_classic
print(f'time_classic:{time_classic}')

width = 0.35

fig = plt.figure()
fig.canvas.set_window_title('flow')
plt.bar(np.arange(n) - width / 2, x, width=width)
plt.bar(np.arange(n) + width / 2, x1, width=width)
plt.xticks(range(n), ['route {0}'.format(i) for i in range(n)])
plt.xlabel('route')
plt.ylabel('flow')
plt.legend(['MSA', 'optimization'])

fig = plt.figure()
fig.canvas.set_window_title('time')
plt.bar(np.arange(n) - width / 2, ttime, width=width)
plt.bar(np.arange(n) + width / 2, time1, width=width)
plt.xticks(range(n), ['route {0}'.format(i) for i in range(n)])
plt.xlabel('route')
plt.ylabel('time')
plt.legend(['MSA', 'optimization'])
plt.show()
