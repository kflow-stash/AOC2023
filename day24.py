import itertools as iter

input_ = open("data/day24.txt", "r").read().splitlines()

lines = {} #((x,y,z),(vx,vy,vz))
min_ = 200000000000000
max_ = 400000000000000
for ix, row in enumerate(input_):
    loc, vec = tuple(tuple(int(y) for y in x.split(", ")) for x in row.split(" @ "))
    slope = vec[1]/vec[0]
    intercept = loc[1] - (loc[0]*slope)
    lines[ix] = (slope,intercept,loc,vec)
    #t = (min_*slope + intercept, max_*slope+intercept)
    #lines[ix] = (min(*t,min_),max(*t,max_))
  
def intersect_(m1,b1,loc1,v1,m2,b2,loc2,v2):
    if m1 == m2 and b2 != b1:
        return False,None
        
    x = (b2-b1)/(m1-m2)
    y = m1*x + b1
    if x <=max_ and x >= min_ and y<= max_ and y>=min_:
        #check if intersection happens in the past
        if (x-loc1[0])*v1[0] < 0 or (x-loc2[0])*v2[0] < 0:
            return False, None
        else:
            return True, (x,y)
    else:
        return False,None
  
n_=0
for l1,l2 in iter.combinations(lines,2):
    t, i_pt = intersect_(*lines[l1],*lines[l2])

    if t:
        n_+=1
        print(l1,l2, i_pt)
    stop_here = 1
    
print(n_)
stop_here =1