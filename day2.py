from collections import defaultdict 
import math
input_ = open('data/day2_pt1.txt','r').read().splitlines()

total_dict = {"red":12,"green":13,"blue":14}

successful_games = []
game_scores = []
for ix, gameline_ in enumerate(input_):
    sets_ = gameline_.split(": ")[1].split("; ")
    
    failed = False
    game_dict = defaultdict(lambda: 0)
    for set_ in sets_:
        set_dict = defaultdict(lambda: 0)
        for draw_ in set_.split(', '):
            for color_, count_ in draw_.split(' '):
                set_dict[color_]+=int(count_) 

        for color_, count_ in set_dict.items():
            game_dict[color_] = max(game_dict[color_],count_)
            if count_ > total_dict[color_]:
                failed=True
        
    if not failed:  
        successful_games.append(ix+1)
    game_scores.append(math.prod([x for x in game_dict.values()]))
        
print("pt1",sum(successful_games))    
print("pt2",sum(game_scores))
    