from collections import deque, defaultdict
import math
input_ = open("data/day20.txt", "r").read().splitlines()

types = {}
map_ = {}
statuses = {}
rem = {}
for ix, row in enumerate(input_):
    t = row[0]
    src, dest = row.split(" -> ")
    map_[src.replace("%","").replace("&","")] = dest.split(", ")
    if t== "%":
        types[src[1:]]="flip" 
        statuses[src[1:]]=0
    elif t == "&":
        types[src[1:]] = "con"
        statuses[src[1:]]=0
    else:
        types[src] = "broadcast"
        
rem = defaultdict(dict)
for con_name,_ in [(k,v) for k,v in map_.items() if types[k] == "con"]:
    for src,dest in map_.items():
        if con_name in dest:
            rem[con_name].update({src:0})

track_nodes = {x:[] for x in rem["qb"].keys()}
def push_button():
    rx_low= 0
    rx_high=0
    low_pulses = 1
    high_pulses = 0
    q = deque([("broadcaster",0)])
    while q:
        orig, signal = q.popleft()
        #print(orig,signal)
        
        
        for dest in map_[orig]:
            if dest == "rx" and signal==0:
                rx_low +=1
            elif dest=="rx" and signal==1:
                rx_high+=1
            
            if signal==0:
                low_pulses+=1
            else:
                high_pulses +=1
            if dest not in types.keys():
                continue
            if types[dest]=="flip" and signal == 0:
                status = statuses[dest]
                statuses[dest] = 1 if status == 0 else 0
                q.append((dest,1 if status == 0 else 0))
            elif types[dest]=="con":
                rem[dest].update({orig:signal})
                states = list(rem[dest].values())
                if sum(states)==len(states):
                    #all remembered states are high - send low pulse
                    statuses[dest] = 0

                    q.append((dest,0))
                else:
                    #send high pulse
                    statuses[dest] = 1
                    if dest in track_nodes.keys():
                        track_nodes[dest].append(pt2_iter)
                    q.append((dest,1))
                    
    
    return low_pulses, high_pulses
low= 0 
high=0
for x in range(1000):
    l,h= push_button()
    low+=l
    high+=h


print("pt1",low*high)

# look for repeated patterns in the nodes leading directly to rx

pushes=0
memo_status = defaultdict(list)
first_status = []
found_sets = set()
for pt2_iter in range(10000):
    
    push_button()
        
    stop_here = 1
    
reps = {}
for dest,vals in track_nodes.items():
    t = [y-x for x,y in zip(vals,vals[1:])]
    reps[dest] = t
    
pt2 = math.lcm(*[x[0] for x in reps.values()])

print("pt2",pt2)
