from scipy.optimize import fsolve, root_scalar
import random
from itertools import combinations
from collections import defaultdict

input_ = open("data/day24.txt", "r").read().splitlines()

lines = []
for ix, row in enumerate(input_):
    loc, vec = tuple(tuple(int(y) for y in x.split(", ")) for x in row.split(" @ "))
    lines.append({'loc': loc, 'vec': vec})


#((x2 + vx2*t2) - (x1 + vx1*t1))*(t3-t1) = ((x3 + vx3*t3) - (x1 + vx1*t1)) * (t2-t1)
def func(args):
    
    t1,t2,t3,t4,t5,t6 = args
    #if abs(t2 - t1)<1 or abs(t3-t1) < 1 or abs(t3-t2)<1:
    #    return [1000,1000,1000]
    #if t1 < 1 or t2 < 1 or t3 < 1:
    #    return [1000,1000,1000]
    func1 = ((x2 + vx2*t2) - (x1 + vx1*t1))/(t2-t1) - ((((x3 + vx3*t3) - (x2 + vx2*t2)) / (t3-t2))) 
    func2 = ((y2 + vy2*t2) - (y1 + vy1*t1))/(t2-t1) - ((((y3 + vy3*t3) - (y2 + vy2*t2)) / (t3-t2))) 
    func3 = ((z2 + vz2*t2) - (z1 + vz1*t1))/(t2-t1) - ((((z3 + vz3*t3) - (z2 + vz2*t2)) / (t3-t2))) 
    func4 = ((x4 + vx4*t4) - (x3 + vx3*t3))/(t4-t3) - ((((x6 + vx6*t6) - (x5 + vx5*t5)) / (t6-t5))) 
    func5 = ((y4 + vy4*t4) - (y3 + vy3*t3))/(t4-t3) - ((((y6 + vy6*t6) - (y5 + vy5*t5)) / (t6-t5))) 
    func6 = ((z4 + vz4*t4) - (z3 + vz3*t3))/(t4-t3) - ((((z6 + vz6*t6) - (z5 + vz5*t5)) / (t6-t5))) 
    #print(args,func1,func2,func3)
    return (func1,func2,func3,func4,func5, func6)

#t = func((4e+11,1e+24,9e+11))
xs = defaultdict(int)
z = 0 
for (line1,line2,line3,line4,line5,line6) in combinations(lines,6):
    print(z)
    z+=1
    (x1, y1, z1) = line1["loc"]
    (vx1, vy1, vz1) = line1["vec"]
    (x2, y2, z2) = line2["loc"]
    (vx2, vy2, vz2) = line2["vec"]
    (x3, y3, z3) = line3["loc"]
    (vx3, vy3, vz3) = line3["vec"]
    (x4, y4, z4) = line4["loc"]
    (vx4, vy4, vz4) = line4["vec"]
    (x5, y5, z5) = line5["loc"]
    (vx5, vy5, vz5) = line5["vec"]
    (x6, y6, z6) = line6["loc"]
    (vx6, vy6, vz6) = line6["vec"]
    
    solution = fsolve(func,x0 = (random.randint(10000000,100000000),random.randint(10000000,100000000),random.randint(10000000,100000000),
                                 random.randint(10000000,100000000),random.randint(10000000,100000000),random.randint(10000000,100000000)),)

    [t1,t2,t3,t4,t5,t6] = solution
    
    if t1 > 0 and t2 >0 and t3>0 and t4>0 and t5 > 0 and t6>0:
        stop_here =1
        t1 = round(t1,0)
        t2 = round(t2,0)
        t3 = round(t3,0)
        t4 = round(t4,0)
        t5 = round(t5,0)
        t6=round(t6,0)

        vx0 = ((x2 + vx2*t2) - (x1 + vx1*t1))/(t2-t1)
        vy0 = ((y2 + vy2*t2) - (y1 + vy1*t1))/(t2-t1)
        vz0 = ((z2 + vz2*t2) - (z1 + vz1*t1))/(t2-t1)
        x1_1 = x1 + vx1*t1 
        y1_1 = y1 + vy1*t1 
        z1_1 = z1 + vz1*t1 

        x0 = x1_1 - (vx0*t1)
        y0 = y1_1 - (vy0*t1)
        z0 = z1_1 - (vz0*t1)
        
        try:
            slt = int(x0+y0+z0)
            
            if slt in xs and xs[slt] > 50:
                stop_here = 1
            xs[slt]+=1
        except:
            pass
    

print(x0+y0+z0)

stop_here = 1