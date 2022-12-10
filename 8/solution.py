import numpy as np

d = (open('data.txt','r')).readlines()
n = len(d[0].strip())
data = np.empty((n,n),int)
for ix,line in enumerate(d):
    for iy,char in enumerate(line.strip()):
        data[ix,iy] = int(char)

def clear(view,tree):
    for i,t in enumerate(view):
        if t>=tree:
            return i + 1
    return len(view)

score = 0
visible = 0
for ix in range(n):
    for iy in range(n):
        views = [np.flip(data[0:ix,iy]), data[ix+1:,iy], np.flip(data[ix,0:iy]), data[ix,iy+1:]]
        visible += int(np.any([np.all(v < data[ix,iy]) for v in views]))
        score = max(score, np.prod([clear(v,data[ix,iy]) for v in views]))
print('1st :', visible)
print('2nd :', score)