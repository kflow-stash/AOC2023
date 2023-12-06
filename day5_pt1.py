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

print('pt1',min(final_seeds))
