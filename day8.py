import itertools as it
import math
input_ = open('data/day8.txt','r').read().replace("(","").replace(")","").splitlines()

mapper = {"R":1,"L":0}
directs = [mapper[x] for x in input_[0]]

map_ = {}
for line_ in input_[2:]:
    key, val = line_.split(" = ")
    map_[key] = val.split(", ")

steps=0
src = "AAA"
for direct_ in it.cycle(directs):
    src = map_[src][direct_]
    steps+=1
    if src == "ZZZ":
        break

print("pt1",steps)

cycle_nums = []
steps=0
srcs = [x for x in map_.keys() if x[-1]=="A"]
for src in srcs:
    for direct_ in it.cycle(directs):
        src = map_[src][direct_]
        steps+=1
        if src[-1] == "Z":
            cycle_nums.append(steps)
            steps =0
            break

lcm = 1
for x in cycle_nums:
    lcm = lcm*x//math.gcd(lcm, x)

print("pt2",lcm)

