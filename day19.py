import math
from copy import deepcopy

maps, ins = open("data/day19.txt", "r").read().split("\n\n")
maps = {x.split("{")[0]:x.split("{")[1][:-1] for x in maps.split("\n")}
  
def eval_(v,x,m,a,s):
    instructs = v.split(",") 
    for i in instructs[:-1]:
        e, t = i.split(":")
        if eval(e) and len(t) == 1:
            return t
        elif eval(e):
            return eval_(maps[t],x,m,a,s)
    if len(instructs[-1])==1:
        return instructs[-1]
    else:
        return eval_(maps[instructs[-1]],x,m,a,s)
            
total = 0
for val_dict in ins.replace("{","").replace("}","").split("\n"):   
    t = [int(x.split("=")[-1]) for x in val_dict.split(",")]
    answer = eval_(maps["in"],*t)  
    if answer == "A":
        total+=sum(t) 

print("pt1",total)

def intersect(a,b,v):
    min_ = max(a[0],b[0])
    max_ = min(a[1],b[1])
    if max_ > min_:
        return {v:(min_,max_)}
    else:
        return {None:None}

def trace(map_,conds):
    cond,tf = map_.split(":",1)
    thresh = int(cond[2:])
    var = cond[0]
    if cond[1] == ">":
        tc =(thresh+1,4001)
        fc = (1,thresh+1)
    else:
        tc = (1,thresh)
        fc = (thresh,4001)
    
    tconds = deepcopy(conds)
    fconds = deepcopy(conds)
    tconds.update(intersect(tc,conds[var],var))
    fconds.update(intersect(fc,conds[var],var))
    
    t,f = tf.split(",",1)
    if t == "A":
        a_paths.append(tconds)
    elif len(t)>1:
        trace(maps[t],tconds)
    
    if f =="A":
        a_paths.append(fconds)
    elif len(f) > 1 and len(f.split(":"))==1:
        trace(maps[f],fconds)
    elif len(f.split(":"))>1:
        conds.update(intersect(fc,conds[var],var))
        trace(f,fconds)

a_paths = []
trace(maps["in"],conds={"a":(1,4001),"m":(1,4001),"s":(1,4001),"x":(1,4001)})        


# compute intersections with unified
# remove intersected ranges from new path
# add new path (minus intersection) back into unified

def dict_intersect(a:dict,b:dict):
    t = {}
    for x in a.keys():
        min_ = max(a[x][0],b[x][0])
        max_ = min(a[x][1],b[x][1])
        if max_ <= min_:
            return False
        t[x] = (min_,max_)
            
    return t

def remove_intersection(src:dict, unified: list):
    for uni in unified:
        intersected = dict_intersect(src,uni)
        if intersected:
            for x, (min_,max_) in intersected.items():
                if max_ > min_:
                    if src[x][0] < min_:
                        src.update({x:(src[x][0],min_)})
                    else:
                        src.update({x:(max_,src[x][1])})
    return src
            
unified = [a_paths[0]]

for src in a_paths[1:]:
    src2 = remove_intersection(deepcopy(src),unified)
    unified.append(src2)
    stop_here = 1

prod_list = [math.prod([x2-x1 for (x1,x2) in y.values()]) for y in unified]

print("pt2",sum(prod_list))
