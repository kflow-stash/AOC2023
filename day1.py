
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
    starting_nums=[]
    ending_nums=[]
    for line_ in input_:
        found_nums = sorted([(line_.find(x),y) for x,y in num_dict.items() if x in line_],key=lambda x:x[0])
        starting_nums.append([str(x[1]) for x in found_nums][0])
        
        found_nums2 = sorted([(line_[::-1].find(x[::-1]),y) for x,y in num_dict.items() if x in line_],key=lambda x:x[0])
        ending_nums.append([str(x[1]) for x in found_nums2][0])
        
    pt2 = sum([int(x+y) for x,y in zip(starting_nums,ending_nums)])
    print("pt2",pt2)
    

