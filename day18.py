import sys
import itertools as iter
from collections import defaultdict
sys.setrecursionlimit(100000)
input_ = open("data/day18.txt", "r").read().splitlines()

vec_dict = {"R": (0,1), "D": (1,0),"U":(-1,0),"L":(0,-1)}
turn_dict = {"UR":"R","RD":"R","DL":"R","LU":"R","RU":"L","DR":"L","LD":"L","UL":"L"}

loc = (0,0)

r_ =0
l_ = 0
x = 0
y = 0
hdict = {'0':'R','1':'D','2':'L','3':'U'}

corners = [(0,0,None)]
total_steps = 0
last_vec = None
for ix,row in enumerate(input_):
    vec, n_steps, col = row.split(" ")
    if ix==0:
        first_vec = vec
    n_steps = int(col[2:-2],16)
    vec = hdict[col[-2]]
    #print(vec,n_steps)

    if last_vec:
        if turn_dict[last_vec+vec] == "R":
            r_+=1
            turn = "R"
        else:
            l_+=1
            turn = "L"
    else:
        turn = None
    last_vec = vec

    corners.append((y,x,turn))

    if vec=="R":
        x += int(n_steps)
    elif vec=="L":
        x += -int(n_steps)
    elif vec =="D":
        y += int(n_steps)
    elif vec=="U":
        y+= -int(n_steps)
        
    total_steps += int(n_steps)
  
minx = min([x for (y,x,d) in corners])
miny = min([y for (y,x,d) in corners])
maxx = max([x for (y,x,d) in corners])
maxy = max([y for (y,x,d) in corners])

if r_ > l_:
    interior_corner="R"
else:
    interior_corner="L"


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst)-(n-1)):
        yield lst[i:i + n] 

area_ = 0
for cx, (c1,c2,c3) in enumerate(chunks(corners + corners[:2],3)):
    x = c2[1]
    dy = c1[0] - c3[0]
    area_+=x*dy
    
   
#easy way using theorems
print(int(abs(area_)/2 - (total_steps//2) + 1 + total_steps)  )

#hard way that almost works but not quite
first_d = turn_dict[vec+first_vec]
z = corners[0]
corners[0] = (z[0],z[1],first_d)
        
ys = sorted(list(set([y for y,_,_ in corners])))
xmin = sys.maxsize
xmax = -sys.maxsize
area = 0

corners_reversed = list(reversed(corners))

pivot =  [(y,x,d) for (y,x,d) in corners if y==ys[0]][0]
clock_index = corners.index(pivot)
counter_index = corners_reversed.index(pivot)

corner_cycle_clock = corners[clock_index:] + corners[:clock_index]
corner_cycle_counter = corners_reversed[counter_index:]+corners_reversed[:counter_index]


clock_groups = list(iter.groupby(corner_cycle_clock,key = lambda x: x[0]))
counter_groups = list(iter.groupby(corner_cycle_counter,key = lambda x: x[0]))

iclock = 0
icounter = 0
for y1, y2 in chunks(ys,2):
    #find min and max x within this y range
    
    clock = list(iter.takewhile(lambda x: x[0] == y1,corner_cycle_clock[iclock:]))
    counterclock = list(iter.takewhile(lambda x: x[0] == y1,corner_cycle_counter[icounter:]))
    
    all_ = list([(y,x,d) for (y,x,d) in corners if y==y1])
    
    exterior_ = set(all_).difference(set(clock),set(counterclock))
    if len(exterior_)>0:
        stop_here = 1
      
    if len(clock) > 0:
        xr = clock[-1][1]
        iclock+=len(clock)
        xr_min = min([x for (y,x,d) in clock])
    else:
        xr_min = xr
    
    if len(counterclock)>0:
        xl = counterclock[-1][1]
        icounter+=len(counterclock)
        xl_max = max([x for (y,x,d) in counterclock])
    else:
        xl_max = xl
        
    gap =  (xr_min - xl_max - 1) if xr_min > xl_max + 1 else 0
    
    area+=(abs(xr - xl)-1)*(y2-y1-1) + gap
    
    print(y1,xl, y2,xr, area)
    
    
print(area + total_steps)
  
stop_here = 1


