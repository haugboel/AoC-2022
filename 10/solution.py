import numpy as np
image = np.zeros([40,6],dtype=int)
with open('data.txt','r') as file:
    signal = []
    X = 1
    cycle = 0
    for line in file:
        cycle += 1
        signal.append(X*cycle)
        instruction = line[0:4]
        xpos = (cycle-1) % 40
        ypos = (cycle-1) // 40
        image[xpos,ypos] = abs(xpos-X)<=1
        if cycle < 20:
            print('Cycle: {:0}, instruction {:1}, value: {:2} signal: {:3}'.format( \
                    cycle,line[0:4],X,signal[-1]))
        if instruction=='addx':
            cycle += 1
            signal.append(X*cycle)
            xpos = (cycle-1) % 40
            ypos = (cycle-1) // 40
            image[xpos,ypos] = abs(xpos-X)<=1
            Y = int(line[4:].strip())
            if cycle < 20:
                print('Cycle: {:0}, instruction {:1}, value: {:2} signal: {:3} reg: {:4}'.format( \
                        cycle,line[0:4],X,signal[-1],Y))
            X = X + Y
# Find the signal strength during the 
# 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
# What is the sum of these six signal strengths?
signal = np.array(signal)
# 12760 too low
print(np.sum(signal[[19,59,99,139,179,219]]))
for y in range(6):
    line = ''
    for x in range(40):
        if image[x,y]==0:
            line += ' '
        else:
            line += '#'
    print(line)
