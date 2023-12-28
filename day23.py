import itertools as iter
import sys
from copy import copy,deepcopy
from collections import defaultdict
sys.setrecursionlimit(10000)

grid = [list(x) for x in open("data/day23.txt", "r").read().splitlines()]

ym = len(grid)
xm = len(grid[0])

s_loc = (0,grid[0].index("."))
dest = (len(grid)-1,grid[-1].index("."))
#dest = (133,127)

def in_bounds(y,x):
    if y < ym and y >=0 and x < xm and x>=0:
        return True
    else:
        return False

final_paths = []
vecs = set([(0,1),(1,0),(-1,0),(0,-1)])
vec_dict = {">":(0,1),"^": (-1,0),"<":(0,-1),"v":(1,0)}

wormholes = defaultdict(set) # end_location, n_steps

def find_wormholes(loc,last,junctions: dict,wormhole:bool,wormhole_start: tuple, n_wormhole_steps: int):
    steps = [(y,x) for y,x in map(lambda x: (x[0][0] + x[1][0],x[0][1]+x[1][1]),zip(vecs,iter.repeat(loc))) if in_bounds(y,x) 
             and grid[y][x] !="#"
             and (y,x) != last]
        
    n_steps = len(steps)
    if n_steps==1:
        if not wormhole:
            wormhole_start=last
            wormhole = True
        n_wormhole_steps+=1
    elif wormhole: # wormhole ends at junction
        skip=False
        if wormhole_start in wormholes.keys():
            if (loc,n_wormhole_steps) in wormholes[wormhole_start]:
                skip = True

        if not skip:
            wormholes[wormhole_start].add((loc,n_wormhole_steps))
            wormholes[loc].add((wormhole_start, n_wormhole_steps))
        
            print(f"new wormhole found. src: {wormhole_start}. dest: {loc}. n_steps: {n_wormhole_steps}")
        else:
            return
        wormhole=False
        n_wormhole_steps=0
        
    steps = [x for x in steps if x not in junctions.keys()]

    for (y_,x_) in steps:
            
        if (y_,x_) == dest:
            #n_steps = sum(junctions.values()) + n_wormhole_steps
            #final_paths.append(n_steps)
            n_wormhole_steps+=1
            wormholes[wormhole_start].add((dest,n_wormhole_steps))
            wormholes[dest].add((wormhole_start, n_wormhole_steps))
            print(f"destination wormhole found. src: {wormhole_start}. dest: {dest}. n_steps: {n_wormhole_steps}")
            return
        else:
            find_wormholes((y_,x_),loc,junctions,wormhole,wormhole_start,n_wormhole_steps)

find_wormholes(s_loc,s_loc,junctions={},wormhole=True,wormhole_start=s_loc,n_wormhole_steps=-1)

stop_here = 1

paths = set()
path_lengths = []
def wormhome(loc,path:dict):
    for cand_worms in wormholes[loc]:
        if cand_worms[0] == dest:
            path_ = deepcopy(path)
            path_[cand_worms[0]] = cand_worms[1]
            paths.add(tuple((x,y) for x,y in path_.items()))
            path_lengths.append(sum(path_.values()) + len(path_.values())-1)
            if len(paths) % 100 == 0:
                print(len(paths))
                print(max(path_lengths))
        elif cand_worms[0] not in path.keys():
            path_ = deepcopy(path)
            path_[cand_worms[0]] = cand_worms[1]
            wormhome(cand_worms[0],path_)

wormhome(s_loc,path={})
#5982 is incorrect
stop_here = 1

def follow(loc,last,junctions: dict,wormhole:bool,wormhole_start: tuple, n_wormhole_steps: int):

    # junctions loc: n_steps from last junction
    if loc in wormholes.keys():
        new_loc, n_steps = wormholes[loc]
        loc = new_loc
        wormhole = False
        junctions[loc] = n_wormhole_steps
        n_wormhole_steps = 0

    """
    if grid[loc[0]][loc[1]] in vec_dict.keys():
        vec_ = [vec_dict[grid[loc[0]][loc[1]]]]
    else: 
        vec_ = vecs
    """
    steps = [(y,x) for y,x in map(lambda x: (x[0][0] + x[1][0],x[0][1]+x[1][1]),zip(vecs,iter.repeat(loc))) if in_bounds(y,x) 
             and grid[y][x] !="#"
             and (y,x) != last]
        
    n_steps = len(steps)
    if n_steps==1:
        if not wormhole:
            wormhole_start=last
            wormhole = True
        n_wormhole_steps+=1
    elif wormhole: # wormhole ends at junction
        wormholes[wormhole_start] = (loc,n_wormhole_steps)
        wormholes[loc] = (wormhole_start, n_wormhole_steps)
        
        print(f"new wormhole found. src: {wormhole_start}. dest: {loc}. n_steps: {n_wormhole_steps}")
        
        wormhole=False
        
    steps = [x for x in steps if x not in junctions.keys()]

    for (y_,x_) in steps:
            
        if (y_,x_) == dest:
            n_steps = sum(junctions.values()) + n_wormhole_steps
            final_paths.append(n_steps)
            return
        else:
            follow((y_,x_),loc,junctions,wormhole,wormhole_start,n_wormhole_steps)
                
                
follow(s_loc,s_loc,junctions={},wormhole=True,wormhole_start=s_loc,n_wormhole_steps=0)

max_len = max([len(x) for x in final_paths])
print(max_len)

"""
path_ = [x for x in final_paths if len(x)==max_len][0]

for y,x in path_:
    grid[y][x]="O"
    
print("\n".join("".join([x for x in y]) for y in grid))
"""

stop_here = 1
            