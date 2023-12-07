from collections import Counter
from functools import cmp_to_key

val_dict = {x:y for x,y in zip(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'],range(13,0,-1))}

input_ = open("data/day7.txt", "r").read().splitlines()

hands = [x.split(" ") for x in input_]

def hand_compare(h1,h2):
    x = h1[1]
    y = h2[1]
    if pt2:
        x_vals = [b for a,b in h1[0] if a!="J"]
        y_vals = [b for a,b in h2[0]  if a!="J"]
        if len(x_vals)>0:
            x_vals[0]+=len([a for a in x if a =="J"])
        else:
            x_vals.append(5)
        if len(y_vals)>0:
            y_vals[0]+=len([a for a in y if a =="J"])
        else:
            y_vals.append(5)
    else:
        x_vals = [b for _,b in h1[0]]
        y_vals = [b for _,b in h2[0]]
    
    for ix in range(min(len(x_vals),len(y_vals),2)):
        if x_vals[ix]>y_vals[ix]:
            return 1
        elif y_vals[ix]>x_vals[ix]:
            return -1

    for ix in range(len(x)):
        if val_dict[x[ix][0]]>val_dict[y[ix][0]]:
            return 1
        elif val_dict[y[ix][0]]>val_dict[x[ix][0]]:
            return -1
        
    return 0

pt2=False
card_counts = [(sorted(Counter(x).items(),key = lambda x_: x_[1],reverse=True),x,int(y)) for x,y in hands]
sorted_ = sorted(card_counts,key=cmp_to_key(hand_compare))

score= 0
for rank_, (hand,raw_,bid) in enumerate(sorted_):
    score+=(rank_+1)*bid

print("pt1",score)

val_dict = {x:y for x,y in zip(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J'],range(13,0,-1))}

pt2=True
card_counts = [(sorted(Counter(x).items(),key = lambda x_: x_[1],reverse=True),x,int(y)) for x,y in hands]
sorted_ = sorted(card_counts,key=cmp_to_key(hand_compare))

score= 0
for rank_, (hand,raw_,bid) in enumerate(sorted_):
    score+=(rank_+1)*bid

print("pt2",score)
