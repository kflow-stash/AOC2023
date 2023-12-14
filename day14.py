input_ = open("data/day14.txt", "r").read().replace(".","0").replace("O","1").replace("#","2").splitlines()

cols = [list(reversed(("2",) + x)) for x in zip(*input_)]

val_ = 0
for col in cols:
    last_ix = 0
    for ix in [ix for ix, v in enumerate(col) if v[0] == "2"]:
        n = len([y for y in col[last_ix:ix] if y == "1"])
        t = sum(range(ix,ix-n,-1))
        last_ix = ix
        val_+=t

print("pt1",val_)

def roll_row(a):
    c = []
    last_ix = 0
    for ix in [ij+1 for ij, v in enumerate(a + [2]) if v == 2]:
        c.extend(list(sorted([x for x in a[last_ix:ix]])))
        last_ix = ix
    return c
   
def roll(grid):
    # roll north
    cols = []
    for col in [list(x) for x in map(reversed,zip(*grid))]:
        cols.append(roll_row(col))
    # roll west
    rows = []
    for row in [list(x) for x in map(reversed,zip(*cols))]:
        rows.append(roll_row(row)) 
    # roll south
    cols = []
    for row in [list(x) for x in map(reversed,zip(*rows))]:
        cols.append(roll_row(row)) 
    # roll east 
    rows = []
    for col in [list(x) for x in map(reversed,zip(*cols))]:
        rows.append(roll_row(col)) 
    return rows
          
result_list = []
grid = [[int(y) for y in x] for x in input_]
first_repeat = None
while not first_repeat:
    grid = roll(grid)
    locs = {(ix,iy) for ix, x in enumerate(grid) for iy,y in enumerate(x) if y==1}
    
    if locs not in result_list:
        result_list.append(locs)
    else:
        first_repeat = result_list.index(locs)
        break

repeat_length = len(result_list) - first_repeat
remainder = (1000000000 - first_repeat) % repeat_length
map_index = remainder + first_repeat

all_ys = [len(grid)-y for (y,_) in list(result_list[map_index-1])]


print("pt2",sum(all_ys))