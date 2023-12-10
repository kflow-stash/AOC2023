input_ = [[int(y) for y in x.split(" ")]  for x in open('data/day9.txt','r').read().splitlines() ]
sum_1 = 0
sum_2=0
for seq in input_:
    zeros=False
    rows=[seq]
    while not zeros:
        rows.append([rows[-1][x+1]-rows[-1][x] for x in range(len(rows[-1])-1)])
        zeros = True if max([abs(x) for x in rows[-1]])==0 else False

    next_num = 0
    for row in rows:
        next_num += row[-1]
        
    f_num = 0
    for row in reversed(rows):
        f_num = row[0]-f_num
    
    sum_1+=next_num
    sum_2+=f_num

print("pt1",sum_1)
print("pt2",sum_2)

