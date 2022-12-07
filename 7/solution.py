class node_class():
    def __init__(self):
        self.folders = []
        self.total_size = 0

def read_folder(node,file):
    words = file.readline().split()
    while words != [] and words[-1] != '..':
        if words[1]=='cd': # move to different folder
            folder = node_class()
            read_folder(folder,file)
            node.folders.append(folder)
            node.total_size += folder.total_size
            words = file.readline().split()
        elif words[1] == 'ls': # list content of folder
            words = file.readline().split()
            while words != [] and words[0] != '$':  # loop until next command
                if words[0] != 'dir': # if dir do nothing
                    node.total_size += int(words[0])
                words = file.readline().split()
    return

# cumulative sum of total_size <= 100000
def sum_nodes(node):
    csum = 0
    for n in node.folders:
        csum += sum_nodes(n)
    if node.total_size <= 100000:
        csum += node.total_size
    return csum

# find best folder to delete
def scan_nodes(node,minsize):
    best_guess = node.total_size
    for n in node.folders:
        if n.total_size > minsize:
            best_guess = min(scan_nodes(n,minsize),best_guess)
    return best_guess

root = node_class()
with open('data.txt','r') as file:
    l = file.readline() # skip first line
    read_folder(root,file)

print('1st: ',sum_nodes(root))

space = 70000000
needed = 30000000
to_be_deleted = root.total_size - (space - needed)

print('2nd:',scan_nodes(root,to_be_deleted))