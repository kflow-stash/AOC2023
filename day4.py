import itertools as it
from collections import defaultdict 
input_ = open('data/day4_pt1.txt','r').read().splitlines()


total_score=0
card_scores={}
for ix, card in enumerate(input_):
    _, [winning_nums, my_nums] = [x.replace("  "," ").split(" | ") for x in card.split(":")]
    winning_nums = [x.strip() for x in winning_nums.split(" ")]
    my_nums = [x.strip() for x in my_nums.split(" ")]
    
    my_winning = [x for x in my_nums if x in winning_nums]
    
    if len(my_winning)>0:
        total_score+=int(2**(len(my_winning)-1))
        card_scores[ix] = (int(2**(len(my_winning)-1)),len(my_winning),1)
    else:
        card_scores[ix] = (0,0,1)

print('pt1',total_score)

total_count = 0
for ix, (score_, n_win, count_) in card_scores.items():
    for cd in range(count_):
        for xd in range(ix+1,min(ix+n_win+1,len(input_))):
            total_count+=1
            (_a,_b, _c) = card_scores[xd]
            card_scores[xd] = (_a,_b, _c+1) 
        
print('pt2',total_count+len(input_))
