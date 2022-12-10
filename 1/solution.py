import numpy as np

supply = []
s = 0
with open('data.txt') as f:
    for l in f.readlines():
        if l == '\n':
            supply.append(s)
            s=0
        else:
            s+=int(l)
supply = np.array(supply)
print('Max calories: ',np.argmax(supply)+1,max(supply))
print((np.sort(supply))[-3:].sum())
