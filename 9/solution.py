import numpy as np

def move_rope(head,tail):
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
    moves = {'R': [1,0],'L': [-1,0],'U': [0,1],'D': [0,-1]}
    knots[0] += moves[m]
    for i in range(knots.shape[0]-1):
        knots[i:i+2] = move_rope(knots[i],knots[i+1])
    return knots

def make_rope(nknots):
    knots = np.zeros((nknots,2))
    #tail_positions = [(0,0)]
    with open('data.txt','r') as file:
        for step, l in enumerate(file):
            for i in range(int(l[1:].strip())):
                knots = move_rope2(l[0],knots)
                tail_positions.append(tuple(knots[-1]))
    return len(set(tail_positions))

print("1st :", make_rope(2), "2nd :", make_rope(10))