import numpy as np

def make_rope(nknots):
    knots = np.zeros((nknots,2))        # allocate knot positions
    tail_positions = {(0,0)}            # start position of tail
    with open('data.txt','r') as file:  # open file
        for line in file:               # loop over instructions
            for i in range(int(line[1:].strip())):   # loop over the number of times a step is to be taken
                knots[0] += {'R': [1,0],'L': [-1,0],'U': [0,1],'D': [0,-1]}[line[0]] # move the head knot
                for i in range(knots.shape[0]-1):                                    # loop over knots
                    if (abs(knots[i,0]-knots[i+1,0]) > 1) or (abs(knots[i,1]-knots[i+1,1]) > 1): # test if rope is breaking
                        knots[i+1] += np.clip(knots[i]-knots[i+1],-1,+1) # move tail knot accordingly. Max one move
                tail_positions.add(tuple(knots[-1])) # add tail position to set
    return len(tail_positions)                       # return length of set

print("1st :", make_rope(2), "2nd :", make_rope(10))