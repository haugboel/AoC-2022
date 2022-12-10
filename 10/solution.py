with open('data.txt','r') as file:
    image = ''
    first = 0
    X = 1
    cycle = 0
    for line in file:
        cycle += 1
        if cycle in (20,60,100,140,180,220): first += X*cycle
        image += {False:' ', True:'#'}[abs(((cycle-1) % 40) - X)<=1]
        if line[0:4]=='addx':
            cycle += 1
            if cycle in (20,60,100,140,180,220): first += X*cycle
            image += {False:' ', True:'#'}[abs(((cycle-1) % 40) - X)<=1]
            X = X + int(line[4:].strip())
print('1st part: ', first)
for i in range(0, len(image), 40): print(image[i:i+40])