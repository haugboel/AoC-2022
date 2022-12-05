# 1st round
score=0
with open('data.txt') as f:
    for ll in f.readlines():
        l = ll.strip()
        c = ord(''.join(set(l[0:len(l)//2]).intersection(l[len(l)//2:])))
        if (c>=97):
            score += (c-97)+1
        else:
            score += (c-65)+27
print('1st round:',score)
#2nd round
score=0
with open('data.txt') as f:
    ll = f.readlines()
    for i in range(len(ll)//3):
        a = ll[3*i].strip()
        b = ll[3*i+1].strip()
        c = ll[3*i+2].strip()
        d=ord(''.join(set(''.join(set(a).intersection(b))).intersection(c)))
        if (d>=97):
            score += (d-97)+1
        else:
            score += (d-65)+27
print('2nd round:',score)
