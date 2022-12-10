import numpy as np
with open('data.txt','r') as file:
    image = ''
    signal = []
    X = 1
    cycle = 0
    for line in file:
        cycle += 1
        signal.append(X*cycle)
        instruction = line[0:4]
        image += {False:' ', True:'#'}[abs((cycle-1) % 40-X)<=1]
        if instruction=='addx':
            cycle += 1
            signal.append(X*cycle)
            image += {False:' ', True:'#'}[abs((cycle-1) % 40-X)<=1]
            X = X + int(line[4:].strip())
print(np.sum(np.array(signal)[[19,59,99,139,179,219]]))
for i in range(0, len(image), 40):
    print(image[i:i+40])