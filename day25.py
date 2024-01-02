from collections import defaultdict
from copy import deepcopy
import sys
from sys import maxsize as INT_MAX
from collections import deque
sys.setrecursionlimit(10000)
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
    found = False
    parents = defaultdict(list)
    q = deque()
    q.append((0,n1))
    while q and not found:
        node_dist, node = q.popleft()
        print(node,nodes[node])
        for vert in nodes[node]:
            if vert==n1 and vert != parents[node]:
                parents[vert] = node
                q.clear()
                found=True
                break
            elif dist[vert] >= node_dist+1:
                q.append((node_dist+1,vert))
                dist[vert] = node_dist+1
                parents[vert]=node
    if found:
        path = set([node])
        p = node
        while p != n1:
            p = parents[p]
            path.add(p)
    else:
        stop_here = 1

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
    
print(len(cycle1),len(cycle2))   
    
snips = list()
for node1, v in nodes.items():
    for node2 in v:
        if (node1 in cycle1 and node2 in cycle2) or (node1 in cycle2 and node2 in cycle1):
            snips.append((node1,node2))
        

found_splits = []
splits = {}

for node1,v in nodes.items():
    for node2 in v:
        
        split = tuple(sorted([node1,node2]))
        if split not in splits:
        # get sets of items on either side of the split
            if split == ('jqt','nvd'):
                stop_here = 1
            
            n_ties = count_ties(split[0],split,net=[split[0]])
            
            if n_ties<3:
                print(split,n_ties)
            
            #net1 = get_net(split[0],split[1],net=set())
            ##print(" ")
            #net2 = get_net(split[1],split[0],net=set())
            #inet = net1.intersection(net2)
            
            
            #splits[split] = {'net1':deepcopy(net1),'net2':deepcopy(net2),'inet':deepcopy(inet),'n_inter':len(inet)}
  
min_split1 = sorted(splits.items(),key=lambda x: x[1]["n_inter"])[0]
found_splits.append(min_split1[0])


#examine the splits of the intersection
splits = {}
for node1 in min_split1[1]["inet"]:
    for node2 in nodes[node1]:
        split = tuple(sorted([node1,node2]))
        if split not in splits:
        # get sets of items on either side of the split
            net1 = get_net(split[0],split[1])
            net2 = get_net(split[1],split[0])
            inet = net1.intersection(net2)
            splits[split] = {'net1':net1,'net2':net2,'inet':inet,'n_inter':len(inet)}

min_split = sorted(splits.items(),key=lambda x: x[1]["n_inter"])[0]

stop_here = 1
        

