
part1 = False

num_dict = {str(x):x for x in range(10)}
word_dict = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

with open('data/day1_pt1.txt','r') as f:
        input_ = f.read().splitlines()
        
if part1:
    
    val = 0
    for line_ in input_:
        nums = [num_dict[x] for x in line_ if x in num_dict.keys()]
        val += int(str(nums[0])+str(nums[-1]))
        
    print('part1',val)
else:
    num_dict.update(word_dict)   

    val = 0
    for line_ in input_:
        #find first instance of all keys in the line, then sort by the found index
        forward_nums = sorted([(line_.find(x),y) for x,y in num_dict.items() if x in line_],key=lambda x:x[0])
        
        #reverse the line and the dictionary keys, then perform the same action
        backward_nums = sorted([(line_[::-1].find(x[::-1]),y) for x,y in num_dict.items() if x in line_],key=lambda x:x[0])
        
        val += int(str(forward_nums[0][1])+str(backward_nums[0][1]))
        
    print("pt2",val)
    

