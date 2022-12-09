import numpy as np

def move_rope(m,head,tail,move=True):
    if move:
        if m=='R':
            head[0] += 1
        if m=='L':
            head[0] -= 1
        if m=='U':
            head[1] += 1
        if m=='D':
            head[1] -= 1
    if (abs(head[0]-tail[0]) > 1) or (abs(head[1]-tail[1]) > 1):
        hor_move = False
        ver_move = False
        if abs(head[0]-tail[0]) > 1:
            tail[0] = (head[0]+tail[0])//2
            hor_move = True
        if (abs(head[1]-tail[1]) > 1):
            tail[1] = (head[1]+tail[1])//2
            ver_move = True
        if abs(head[0]-tail[0]) == 1 and abs(head[0]-tail[0]) == 1: # we are still diagonal
            if not hor_move:
                tail[0] = head[0]
            if not ver_move:
                tail[1] = head[1]
    return np.copy(head), np.copy(tail)

def move_rope2(m,k):
    knots = np.copy(k)
    for i in range(knots.shape[0]-1):
        head, tail = move_rope(m,knots[i],knots[i+1],move=(i==0))
        knots[i]   = np.copy(head)
        knots[i+1] = np.copy(tail)
    return knots

def make_rope(nknots):
    knots = np.zeros((nknots,2))
    tail_positions = [[0,0]]
    with open('data.txt','r') as file:
        for step, l in enumerate(file):
            move = l[0]
            times = int(l[1:].strip())
            for i in range(times):
                knots = move_rope2(move,knots)
                tail_positions.append(knots[-1])
    pos = np.array(tail_positions) # make into a 1D list
    mx = pos.max()-pos.min()
    return len(np.unique(pos[:,0] + mx * pos[:,1]))

print("1st :", make_rope(2))
print("2nd :", make_rope(10))