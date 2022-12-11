class monkey_class():
    def __init__(self,l,items):
        for i in (l[1].split())[2:]:
            if i[-1] == ',':
                items.append(int(i[0:-1]))
            else:
                items.append(int(i))
        self.next = len(items)
        self.operator  = (l[2].split())[-2]
        self.operation = (l[2].split())[-1]
        if self.operator=='+':
            self.option = 1
            self.operation = int(self.operation)
        if self.operator=='*':
            if len(self.operation)==3: # have to square
                self.option = 0
            else:
                self.option = 2
                self.operation = int(self.operation)
        self.test  = int(l[3].split()[-1])

        self.true  = int(l[4].split()[-1])
        self.false = int(l[5].split()[-1])
        self.dict = {False: self.false, True:self.true}
        
        self.business = 0

    def throw(self,i,im,monkeys,itemlist,relief,tests):
        if self.option == 0:
            new = (itemlist[im][i]*itemlist[im][i]) // relief
        if self.option == 1:
            new = (itemlist[im][i] + self.operation) // relief
        if self.option == 2:
            new = (itemlist[im][i] * self.operation) // relief
        recv = self.dict[(new % self.test) == 0]
        next = monkeys[recv].next
        itemlist[recv][next] = new % tests
        monkeys[recv].next += 1

def monkey_operations(relief,rounds):
    lines = (open('data.txt','r')).readlines()
    # process input in monkey blocks
    monkeys = []
    maxitem = 40
    nmonkeys = 8
    itemlist = []
    for n in range(nmonkeys):
        item = []
        for i in range(maxitem):
            item.append(0)
        itemlist.append(item)

    tests = 1
    for i in range(0,len(lines),7):
        items = []
        monkeys.append(monkey_class(lines[i:i+7],items))
        tests *= monkeys[-1].test
        for j, it in enumerate(items):
            itemlist[i//7][j] = it

    for i in range(rounds):
        for im, monkey in enumerate(monkeys):
            for i in range(monkey.next):
                monkey.throw(i,im,monkeys,itemlist,relief,tests)
                monkey.business += 1
            monkey.next = 0

    l = [m.business for m in monkeys]
    l.sort()
    print(l[-1]*l[-2])

monkey_operations(3,20)
monkey_operations(1,10000)