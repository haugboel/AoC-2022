# 2nd round
score=0
# A rock, B paper, C scissor
# X lose, Y draw, and Z win."
with open('data.txt') as f:
    for ll in f.readlines():
        l = ll.strip()
        print(l)
        if l=='A X':
            score +=3+0
        if l=='A Y':
            score +=1+3
        if l=='A Z':
            score +=2+6
        if l=='B X':
            score +=1+0
        if l=='B Y':
            score +=2+3
        if l=='B Z':
            score +=3+6
        if l=='C X':
            score +=2+0
        if l=='C Y':
            score +=3+3
        if l=='C Z':
            score +=1+6
print('2nd round:',score)

# 1st round
score=0
with open('data.txt') as f:
    for l in f.readlines():
        if l[2]=='X': # rock 1 point
            score += 1
            if l[0]=='A': # draw
                score += 3
            if l[0]=='C': # win
                score += 6
        if l[2]=='Y': # paper 2 points
            score += 2
            if l[0]=='A': # win
                score += 6
            if l[0]=='B': # draw
                score += 3
        if l[2]=='Z': # scissor 3 points
            score += 3
            if l[0]=='B': # win
                score += 6
            if l[0]=='C': # draw
                score += 3
print('1st round:',score)
