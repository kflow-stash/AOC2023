from collections import defaultdict 
import math
input_ = open('data/day2_pt1.txt','r').read().splitlines()

total_dict = {"red":12,"green":13,"blue":14}
part1=False
if part1:
    successful_games = []
    for ix, line_ in enumerate(input_):
        sets_ = line_.split(": ")[1].split("; ")
        
        failed = False
        for set_ in sets_:
            set_dict = defaultdict(lambda: 0)
            for draw_ in set_.split(', '):
                set_dict[draw_.split(' ')[1]] += int(draw_.split(' ')[0])
                
            for color_, count_ in set_dict.items():
                if count_ > total_dict[color_]:
                    failed=True
            if failed:
                break
        if not failed:  
            successful_games.append(ix+1)
            
    print("pt1",sum(successful_games))
else:
    game_scores = []
    for ix, line_ in enumerate(input_):
        sets_ = line_.split(": ")[1].split("; ")
        
        failed = False
        game_dict = defaultdict(lambda: 0)
        for set_ in sets_:
            set_dict = defaultdict(lambda: 0)
            for draw_ in set_.split(', '):
                set_dict[draw_.split(' ')[1]] += int(draw_.split(' ')[0])
                
            for color_, count_ in set_dict.items():
                game_dict[color_] = max(game_dict[color_],count_)
                
        game_scores.append(math.prod([x for x in game_dict.values()]))
        
    print("pt2",sum(game_scores))
    