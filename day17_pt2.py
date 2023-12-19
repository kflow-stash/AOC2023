import sys
import itertools as iter
from collections import defaultdict
sys.setrecursionlimit(10000)
from heapq import *
from copy import copy, deepcopy
input_ = open("data/day17.txt", "r").read().splitlines()

grid = []
for y,row in enumerate(input_):
    grid.append([int(x) for x in row])
  
ym = len(grid)
xm = len(grid[0])


def neighs(y,x,vec=None,exc=None):
    vecs = [(0,1),(1,0),(-1,0),(0,-1)]
    if vec:
        t = (-vec[0],-vec[1])
        vecs.remove((-vec[0],-vec[1]))
    if exc:
        vecs.remove(exc)
    
    for y_, x_ in [(y+yd,x+xd) for yd, xd in vecs]:
        if y_ < ym and y_ >=0 and x_ < xm and x_ >= 0:
            yield ((y_,x_), grid[y_][x_])

src = (0,0)
dest = (len(grid)-1,len(grid[0])-1)

q, seen, mins = [(0,src,[],[])], set(), {(src,()): 0}
while q:
    (cost,v1,path,vec_path) = heappop(q)
    vec = (v1[0] - path[0][0],v1[1] - path[0][1]) if path else None
    n_consec = len(list(iter.takewhile(lambda x: x == vec, vec_path)))

    if (v1,vec,n_consec) not in seen:
        
        seen.add((v1,vec,n_consec))
        path.insert(0,v1)
        vec_path.insert(0,vec)


        if v1 == dest: 
            if n_consec>=3:
                break
            else:
                continue
        if n_consec>=9:
            exc = vec_path[0]
        else:
            exc=None
        
        
        for v2, c in neighs(*v1,vec=vec,exc=exc):
            
            vec_ = (v2[0]-v1[0],v2[1]-v1[1])
            n_consec_ = n_consec + 1 if vec_ == vec else 0

            
            if (v2,vec_,n_consec_) in seen or v2 in path: 
                continue
            if vec != None and n_consec<3 and vec_ != vec:
                continue
            prev = mins.get((v2,vec_,n_consec_), None)
            next = cost + c
            if prev is None or next <= prev:
                mins[(v2,vec_,n_consec_)] = next
                heappush(q, (next, v2, copy(path),copy(vec_path)))


print("pt1",cost)


stop_here = 1

