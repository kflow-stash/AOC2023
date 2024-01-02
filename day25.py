from collections import defaultdict
from copy import copy
from sys import maxsize as INT_MAX
from collections import deque
input_ = open("data/day25.txt", "r").read().splitlines()

nodes = defaultdict(set)
for line_ in input_:
    lhs, rhs = line_.split(": ")
    rhs = set(rhs.split(" "))
    nodes[lhs].update(rhs)
    for x in rhs:
        nodes[x].add(lhs)
    
dist = {}      
for vert in nodes.keys():
    dist[vert]=INT_MAX  
    
def shortest_cycle(n1):
    #find the shortest cycle starting at n1 (does not double-back)
    #store the path taken in the queue
    found = False
    parents = defaultdict(list)
    q = deque()
    q.append((0,n1,[]))
    while q and not found:
        node_dist, node,path = q.popleft()
        for vert in nodes[node]:
            if vert==n1 and vert != parents[node]:
                parents[vert] = node
                q.clear()
                found=True
                path.append(n1)
                break
            elif vert not in path:
                p_ = copy(path)
                p_.append(vert)
                q.append((node_dist+1,vert,p_))
                dist[vert] = node_dist+1
                parents[vert]=node

    return frozenset(path)
   
paths = set()
for src in nodes.keys():
    paths.add(shortest_cycle(src))
    
default_ = list(paths)[0]
cycle1 = set(default_)
paths.remove(default_)
cycle2 = set()
adding = True
while adding:
    adding = False
    for path in list(paths):
        if len(cycle1.intersection(path)) > 0:
            cycle1.update(path)
            paths.remove(path)
            adding = True
            break
    
for path in paths:
    cycle2.update(path)
    
print(len(cycle1)*len(cycle2))   
    