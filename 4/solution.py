import re

# 1st round
score=0
with open('data.txt') as f:
    for ll in f.readlines():
        l = ll.strip() # Example 22-65,22-66
        d = [int(ss) for ss in re.findall(r'\d+', l)]
        if ((d[2]>=d[0]) and (d[3]<=d[1])) or (d[0]>=d[2]) and (d[1]<=d[3]):
            score += 1
print('1st round:',score)

# 2nd round
score=0
with open('data.txt') as f:
    for ll in f.readlines():
        l = ll.strip() # Example 22-65,22-66
        d = [int(ss) for ss in re.findall(r'\d+', l)]
        lo1 = d[0]; up1=d[1]; lo2=d[2]; up2=d[3]
        if ((lo2<=up1) and (up2>=lo1)) or ((lo1<=up2) and (up1>=lo2)):
            score += 1
print('2nd round:',score)