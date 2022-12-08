import numpy as np

data = []
d = (open('data.txt','r')).readlines()
for l in d:
    data.append([int(i) for i in l.strip()])
data = np.array(data)
n = data.shape[0]

def clear(line,tree):
    for i,l in enumerate(line):
        if l>=tree:
            return i + 1
    return line.shape[0]

score = 0
visible = n*2+(n-2)*2
for ix in range(1,n-1):
    for iy in range(1,n-1):
        views = [np.flip(data[0:ix,iy]), data[ix+1:,iy], np.flip(data[ix,0:iy]), data[ix,iy+1:]]
        if np.any([np.all(v < data[ix,iy]) for v in views]):
            visible += 1
        score = max(score, np.prod([clear(v,data[ix,iy]) for v in views]))
print('1st :', visible)
print('2nd :', score)