import math
times,distances = open('data/day6.txt','r').read().splitlines()

times = [int(x) for x in times.split(":")[1].split(" ") if x.isdigit()]
records = [int(x) for x in distances.split(":")[1].split(" ") if x.isdigit()]

score = 1
for t,r in zip(times,records):
    ds = 0
    for t_go in range(t):
        ds+=1
    score *= ds
       
t = int(''.join([str(x) for x in times]) )
r = int(''.join([str(x) for x in records]) )

def quad(b,c):
    x1 = (-b + (b**2 - (4*c))**0.5)/2
    x2 = (-b - (b**2 - (4*c))**0.5)/2
    return int(max(x1,x2))-int(min(x1,x2))

print("pt1",score)
print("pt2",quad(-t,r))