import itertools as it
from collections import defaultdict 
input_ = open('data/day3_pt1.txt','r').read().splitlines()

def is_symbol(x:str):
    if (not x.isdigit()) and (x != "."):
        return True
    else:
        return False

def is_adjacent(x,y,matrix):
    offsets = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
    for xd, yd in offsets:
        #lazy way to disregard matrix boundaries
        try:
            if is_symbol(matrix[y+yd][x+xd]):
                return True, (y+yd,x+xd)
        except:
            pass
        
    return False,(0,0)

gears = defaultdict(lambda: [])
sum_ = 0
for y, row_ in enumerate(input_):
    x = 0
    while x < len(row_):
        charnum = list(it.takewhile(lambda x: x.isdigit(),row_[x:]))
        if len(charnum)==0:
            x+=1
        else:
            print(charnum)
            for xloc in range(x,x+len(charnum)):
                adj,symb = is_adjacent(xloc,y,input_)
                if adj:
                    num_ = int(''.join(charnum))
                    sum_ += num_
                    gears[symb].append(num_)
                    break
            x+=len(charnum)
                    
    
                
print('pt1',sum_)

pt2 = 0
for symb, partnums in gears.items():
    if len(partnums)==2:
        pt2+= partnums[0] * partnums[1]
        
print('pt2',pt2)