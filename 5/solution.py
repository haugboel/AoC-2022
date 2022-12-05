import re

# 1st round
read_crates=True
stacks=None
with open('data.txt') as f:
    for ll in f.readlines():
        # read in initial crate distribution
        if read_crates:
            if ll[1]=='1':
                # we are don reading crate distribution.
                # reverse lists to faciulitate moving around crates
                read_crates=False
                for i in range(len(stacks)):
                    stacks[i].reverse()
            else:
                blocks = [ll[i:i+4].strip() for i in range(0, len(ll), 4)]
                if stacks==None:
                    stacks = [[] for _ in range(len(blocks))]
                for i, b in enumerate(blocks):
                    if b !='':
                        stacks[i].append(b[1])
        # read in moves
        else:
            l = ll.strip()
            d = [int(ss) for ss in re.findall(r'\d+', l)]
            for i in range(d[0]):
                # move 1 from 7 to 6
                crate = stacks[d[1]-1].pop(-1)
                stacks[d[2]-1].append(crate)
end_crate = [c[-1] for c in stacks]
print('1st round: '+''.join(end_crate))

# 2nd round
read_crates=True
stacks=None
m = [] # list of crates to be moved in one go
with open('data.txt') as f:
    for ll in f.readlines():
        # read in initial crate distribution
        if read_crates:
            if ll[1]=='1':
                # we are don reading crate distribution.
                # reverse lists to faciulitate moving around crates
                read_crates=False
                for i in range(len(stacks)):
                    stacks[i].reverse()
            else:
                blocks = [ll[i:i+4].strip() for i in range(0, len(ll), 4)]
                if stacks==None:
                    stacks = [[] for _ in range(len(blocks))]
                for i, b in enumerate(blocks):
                    if b !='':
                        stacks[i].append(b[1])
        # read in moves
        else:
            l = ll.strip()
            d = [int(ss) for ss in re.findall(r'\d+', l)]
            for _ in range(d[0]):
                m.append(stacks[d[1]-1].pop(-1))
            for _ in range(d[0]):
                stacks[d[2]-1].append(m.pop(-1))
end_crate = [c[-1] for c in stacks]
print('2nd round: '+''.join(end_crate))