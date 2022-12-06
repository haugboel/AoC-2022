# Alternative one-liner that evaluate all occurences, so slower on large sequences
# message = lambda n,l: [i for i, x in enumerate([len(set(l[i:i+n]))==n for i in range(len(l)-n)]) if x][0]+n

def message(n,l):
    for i in range(len(l)-n):
        if len(set(l[i:i+n]))==n:
            return i+n

l = open('data.txt','r').readline()
print('1st: ',message(4,l))
print('2nd: ',message(14,l))