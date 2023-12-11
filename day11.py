from itertools import combinations

space_ = open('data/day11.txt','r').read().splitlines()

#expand space
e_rows = []
e_cols = []
gals = set()
for y,row in enumerate(space_):
    found=False
    for x, val in enumerate(row):
        if val == "#":
            gals.add((y,x))
            found=True
    if not found:
        e_rows.append(y)

n_cols = len(space_[0])
for x in range(n_cols):
    if len([z[x] for z in space_ if z[x] == "#"])==0:
        e_cols.append(x)

gap_dist = 1000000-1
total_dist = 0
for pt1, pt2 in combinations(gals,2):
    
    h_gap = 0
    z_gap = 0
    for e_row in e_rows:
        if (min(pt1[0],pt2[0])<e_row) and (max(pt1[0],pt2[0])>e_row):
            z_gap+=gap_dist
    for e_col in e_cols:
        if (min(pt1[1],pt2[1])<e_col) and (max(pt1[1],pt2[1])>e_col):
            h_gap+=gap_dist
    
    yd = abs(pt1[0] - pt2[0]) + z_gap
    xd = abs(pt1[1] - pt2[1]) + h_gap
    dist = min(yd,xd)*2 + abs(yd-xd)
    
    total_dist+=dist

print(total_dist)
