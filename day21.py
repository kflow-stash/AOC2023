from collections import deque, defaultdict
import itertools as iter
from copy import copy,deepcopy
import numpy as np
input_ = open("data/day21.txt", "r").read().splitlines()

ym = len(input_)
xm = len(input_[0])
#input is completely square and starting location is the center

grid0 = [["." for _ in range(xm)] for _ in range(ym)]

rocks = set()
loc_init = set()
for iy, row in enumerate(input_):
    for ix, cell in enumerate(row):
        grid0[iy][ix] = cell
        if cell == "#":
            rocks.add((iy,ix))
        elif cell == "S":
            loc_init.add( (iy,ix) )
         
vecs = [(0,1),(0,-1),(1,0),(-1,0)]

def in_bounds(yi,xi):
    if (yi<ym) and (yi>=0) and (xi<xm) and (xi>=0):
        return True
    else:
        return False
    
def take_step(yi,xi):
    for vec in vecs:
        y,x = yi + vec[0],xi+vec[1]
        if (
            in_bounds(yi+vec[0],xi+vec[1])
            and 
            (y,x) not in rocks
        ):
            loc1.add((y,x))
pt1=False
if pt1: 
    loc0 = copy(loc_init)
    #testing different seed loc
    for _ in range(340):   
        loc1 = set()      
        for loc in loc0:
            take_step(*loc)
            
        loc0 = copy(loc1)
        #print(_,len(loc1))
        if len(loc1) == 7424:
            print(_,len(loc1))
            break
                
    print("pt1",len(loc1))
    stop_here = 1


def take_step2(yi,xi,map_):
    for vec in vecs:
        y,x = (yi + vec[0]),(xi+vec[1])
        if y ==ym:
            map2 = (map_[0]+1,map_[1])
            y = 0
        elif y < 0:
            map2 = (map_[0]-1,map_[1])
            y = ym-1
        elif x == xm:
            map2 = (map_[0],map_[1]+1)
            x = 0
        elif x < 0:
            map2 = (map_[0],map_[1]-1)
            x = xm-1
        else:
            map2 = map_
            
        if map2 in saturated.keys():
            continue    
        
        #must check to see if already occupied on the same level
        if (
            (y,x) not in rocks
        ):
            loc1.add((y,x, map2))


loc0 = copy(loc_init)
locs0 = set()
locs0.add((*list(loc0)[0],(0,0)))

maps = set()
maps.add((0,0))
saturated = dict() #(iterations at saturation, last val, 2nd last val)

n_steps = 26501365

n_block_steps = n_steps // xm

total_blocks = 1
for x in range(n_block_steps+1,1,-1):
    total_blocks+=(x-1)*4
    
total_steps = total_blocks * 7406 #saturation value   

rem = n_steps - (n_block_steps * xm)

from collections import Counter
sat0 = False
add_count = 1
map_count_lists = defaultdict(list)
rem_dict = {}
for it_ in range(500):   
    loc1 = set()
    
    for loc in locs0:
        take_step2(*loc)
    

    map_counts = Counter([z for _,_,z in loc1])
    for map_, count_ in map_counts.items():
        map_count_lists[map_].append(count_)
    if sat0:
        add_count+=1
        
    if add_count == rem:
        rem_dict = {x:y[-1] for x,y in map_count_lists.items() if x != (0,0)}
        break
    
    for map_, cl in map_count_lists.items():
        t = list(reversed(list(iter.batched(cl,n=2))))
    
        if len(t)>10 and t[0] == t[1]:
            if map_ == (1,0):
                sat0 = True
            if map_ in saturated.keys():
                stop_here = 1
            saturated[map_] = (it_,len(cl),cl[-1],cl[-2])
            continue
    
    for k in saturated.keys():
        if k in map_count_lists:
            del map_count_lists[k]


    locs0 = [(y,x,z) for y,x,z in loc1 if z not in saturated.keys()]
    print(it_)

#edges and corners and then add the rest of the blocks

remainder = sum([x for x in rem_dict.values()][:8]) + ((sum([x for x in rem_dict.values()][8:])/(len(rem_dict.values())-8))*((n_block_steps-1)-8)/8)

pt2 = total_steps + remainder
            
stop_here = 1