from collections import defaultdict

rows = open('data/day10.txt','r').read().splitlines()
mat = [[*y] for y in rows]

map_ = {"|":[0,1,0,1],"-":[1,0,1,0],"L":[0,1,1,0],"J":[1,1,0,0],"7":[1,0,0,1],"F":[0,0,1,1],".":[0,0,0,0],"S":[1,1,1,1]}
graph = defaultdict(lambda: [])
for y,row in enumerate(mat):
    for x,cell in enumerate(row):
        [w,n,e,s] = map_[cell]
        if w==1:
            graph[(y,x)].append((y,x-1))
        if n == 1:
            graph[(y,x)].append((y-1,x))
        if e == 1:
            graph[(y,x)].append((y,x+1))
        if s == 1:
            graph[(y,x)].append((y+1,x))
        if cell == "S":
            s_loc = (y,x)

graph[s_loc] = [x for x,y in graph.items() if s_loc in y]
mat[s_loc[0]][s_loc[1]] = "L"
graph = dict(graph)

visited_nodes = set()

cell = s_loc
found=False
while not found:
    edges = [x for x in graph[cell] if cell in graph[x] and x not in visited_nodes]
    if len(edges)==0:
        found=True
    else:
        visited_nodes.add(edges[0])
        cell = edges[0]

print("pt1",(len(visited_nodes)) // 2)

int_nodes = 0
for y, row in enumerate(mat):
    walls = 0
    for x, cell in enumerate(row):
        if (y,x) in visited_nodes:
            walls+=map_[cell][1]
        else:
            if walls % 2 == 1:
                int_nodes+=1
            
print("pt2",int_nodes)