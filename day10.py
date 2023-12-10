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

visited_nodes = [s_loc]

cell = s_loc
found=False
while not found:
    edges = [x for x in graph[cell] if cell in graph[x] and x not in visited_nodes]
    if len(edges)==0:
        found=True
    else:
        visited_nodes.append(edges[0])
        cell = edges[0]

print("pt1",(len(visited_nodes)) // 2)


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]
        
def count_walls(wall_dirs):
    walls = [sum(x) for x in divide_chunks(wall_dirs,2)]
    return len([x for x in walls if x == 0])

int_nodes = []
for y, row in enumerate(mat):
    walls = []
    for x, cell in enumerate(row):
        if (y,x) in visited_nodes:
            if map_[cell][1]==1:
                walls.append(1)
            if map_[cell][3]==1:
                walls.append(-1)
        else:
            t = count_walls(walls)
            if t % 2 == 1:
                int_nodes.append((y,x))
            
print("pt2",len(int_nodes))