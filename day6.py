import math
times,distances = open('data/day6.txt','r').read().splitlines()

times = [int(x) for x in times.split(":")[1].split(" ") if x.isdigit()]
records = [int(x) for x in distances.split(":")[1].split(" ") if x.isdigit()]

def quad(b,c):
    x1 = (-b + (b**2 - (4*c))**0.5)/2
    x2 = (-b - (b**2 - (4*c))**0.5)/2
    return int(max(x1,x2))-int(min(x1,x2))

score = 1
for t,r in zip(times,records):
    score *= quad(-t,r)
       
t = int(''.join([str(x) for x in times]) )
r = int(''.join([str(x) for x in records]) )

print("pt1",score)
print("pt2",quad(-t,r))