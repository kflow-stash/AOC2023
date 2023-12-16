import sys
import itertools as iter
sys.setrecursionlimit(10000)

input_ = open("data/day16.txt", "r").read().splitlines()

mirror_flip1 = lambda x: [(x[1],x[0])]
mirror_flip2 = lambda x: [(-x[1],-x[0])]
split_hor = lambda x: [(0, x[1])] if abs(x[1])>0 else [(0,1),(0,-1)]
split_vert = lambda x: [(x[0], 0)] if abs(x[0])>0 else [(1,0),(-1,0)]
flips = {"\\":mirror_flip1,"/":mirror_flip2,"|":split_vert,"-":split_hor, ".": lambda x: [x]}

def in_bounds(y,x):
    if y>=0 and y < len(input_) and x >=0 and x<len(input_[0]):
        return True
    else:
        return False

def create_path(yo,xo,vec,visited):
    if in_bounds(yo,xo):
        visited.add((yo,xo,vec))
        sym = input_[yo][xo]
        vecs = flips[sym](vec)
        for vec in vecs:
            new_pt = (yo+vec[0],xo+vec[1],vec)
            if new_pt not in visited:
                create_path(*new_pt,visited)            
    return visited
     
visited = create_path(0,0,(0,1),set())
visited_locs = set((x,y) for (x,y,_) in visited)
print("pt1",len(visited_locs))
    
energized = []
def traverse(y,x,initial_vec):
    visited = create_path(y,x,initial_vec,set())
    energized.append(len(set((x,y) for (x,y,_) in visited)))

for loc in zip(iter.repeat(0),range(len(input_[0]))):
    traverse(*loc,(1,0))

for loc in zip(range(len(input_)),iter.repeat(0)):
    traverse(*loc,(0,1))

for loc in zip(iter.repeat(len(input_)-1),range(len(input_[0]))):
    traverse(*loc,(-1,0))
    
for loc in zip(range(len(input_)),iter.repeat(len(input_[0])-1)):
    traverse(*loc,(0,-1))

print("pt2",max(energized))