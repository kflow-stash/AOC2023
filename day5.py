import itertools as it
from collections import defaultdict 
input_ = open('data/day5.txt','r').read()

map_cats = input_.split("\n\n")
seeds = [int(x) for x in map_cats[0].split(": ")[1].split(" ")]

map_dict = defaultdict(lambda:[])
for ix, map_cat in enumerate(map_cats[1:]):
    maps = map_cat.split("\n")[1:]
    for map_ in maps:
        map_code = [int(x) for x in map_.split(' ')]
        map_dict[ix].append((range(map_code[1],map_code[1]+map_code[2]),map_code[0]-map_code[1]))
    
print(map_dict)    

final_seeds = [] 
for seed in seeds:
    for map_ix,map_list in map_dict.items():
        for s_rng,delt in map_list:
            if seed in s_rng:
                seed += delt
                break
    final_seeds.append(seed)


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))       
#pt2_seed_rngs = [range(x,x+y) for x,y in list(chunker(seeds,2))]
pt2_seeds = [x for x,y in list(chunker(seeds,2))]


max_seed = max(seeds)

def rng_overlap(a,b, indelt,outdelt):
    very_bottom = min(min(a),min(b))
    bottom=max(min(a),min(b))
    top = min(max(a),max(b))
    very_top = max(max(a),max(b))
    rngs = {}
    if top > bottom:
        rngs[(bottom,top)] = indelt
        if very_bottom<bottom:
            rngs[(very_bottom,bottom)] = outdelt
        #if very_top > top:
        #    rngs[(top,very_top)] = outdelt
            
    return rngs
    
import copy
def overlapping(a,b_dict,a_delt):
    c_dict = copy.copy(b_dict)
    for b, b_delt in b_dict.items():
        a2 = [x-b_delt for x in a]
        o=rng_overlap(a2,b,a_delt+b_delt,b_delt)
        if len(o.values())>0:
            c_dict.pop(b)
            c_dict.update(o)
            
    return c_dict

#keys are source ranges
map_dict = {(0,max_seed):0}
for ix, map_cat in enumerate(map_cats[1:]):
    maps = map_cat.split("\n")[1:]
    for map_ in maps:
        map_code = [int(x) for x in map_.split(' ')]
        s_rng = (map_code[1],map_code[1]+map_code[2])
        delt = map_code[0]-map_code[1]
        map_dict = overlapping(s_rng,map_dict,delt)
        stop_here = 1

                


print(map_dict)

"""
def rng_overlap(a,b):
    return range(max(min(a),min(b)),min(max(a),max(b))+1)

full_map= {range(0,max_seed):0}
for s_rng, s_delt, d_rng in maps_list:
    for f_rng, f_delt in full_map.items():
        
        if (min(s_rng)<=min(f_rng)) and (max(s_rng)>=min(f_rng)):
            #overlaps (below)
            _ = full_map.pop(f_rng)
            full_map[range(min(s_rng),min(f_rng))] = s_delt
            full_map[range(min(f_rng),max(s_rng))] = s_delt + f_delt
            full_map[range(max(s_rng),max(f_rng))] = f_delt
            
        elif (min(s_rng)>=min(f_rng)) and (max(s_rng)<=max(f_rng)):
            #overlaps (containing)
            _ = full_map.pop(f_rng)
            full_map[range(min(f_rng),min(s_rng))] = f_delt
            full_map[range(min(s_rng),max(s_rng))] = s_delt + f_delt
            full_map[range(max(s_rng),max(f_rng))] = f_delt
            
        elif (min(s_rng)>=min(f_rng)) and (max(s_rng)>=min(f_rng)):
            #overlaps (above)
            _ = full_map.pop(f_rng)
            full_map[range(min(f_rng),min(s_rng))] = f_delt
            full_map[range(min(s_rng),max(f_rng))] = s_delt + f_delt
            full_map[range(min(s_rng),max(f_rng))] = s_delt + f_delt

        
        if max(s_rng)<max(f_rng):
            _=full_map.pop(f_rng)
            #lower non-overlapping
            full_map[range(min(f_rng),min(s_rng))] = f_delt
            #overlapping
            full_map[range(min(s_rng),)]
    

"""
#print('pt1',min(final_seeds))
print('pt2',min(final_seeds))