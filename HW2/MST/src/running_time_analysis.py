import numpy as np
import matplotlib.pyplot as plt
import glob
from collections import defaultdict
import matplotlib.ticker as ticker

# read the file for the number of edges
edges = defaultdict(list)
i = 0
with open('../output.txt','r') as f:
    for line in f:
        if i % 9 == 0:
            filename = line.split(' ')[1][:-1]
        if i % 9 == 3:
            edges[filename].append(int(line.split(' ')[-1]))
        i += 1


for output in glob.glob("../results/*.txt"):
    filename = (output.split('/')[2]).split('_')[0]
    i = 0
    total_time = 0
    with open(output,'r') as f:
        for line in f:
            time = float(line.split(' ')[1][:-2])
            if i == 0:
                edges[filename].append(time)
            else:
                total_time += time
            i += 1
        edges[filename].append(total_time)

# print(edges.values())
data = np.array([t for t in edges.values()])
fig, ax = plt.subplots()
ax.plot(data[:,0],data[:,1]/1000,'-*')
plt.xlabel('number of edges |E|')
plt.ylabel('computation time (in seconds)')
plt.title('Static computation time')
ax.set_xscale('log')

plt.show()
# print(data)

fig, ax = plt.subplots()
ax.plot(data[:,0],data[:,2]/1000,'-*')
plt.xlabel('number of edges |E|')
plt.ylabel('computation time (in seconds)')
plt.title('Dynamic computation time')
ax.set_xscale('log')

plt.show()




    
