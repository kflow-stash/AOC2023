from collections import defaultdict,OrderedDict
input_ = open("data/day15.txt", "r").read().replace("-","=")

words = input_.split(",")

def hash_(word):
    h = 0
    for char_ in word:
        h+=ord(char_)
        h*=17
        h=h % 256
    return h

bins = []
boxes = defaultdict(lambda:[])
for word in words:
    bins.append(hash_(word))
    t = word.split("=")
    label = t[0]
    operation_ = int(t[1]) if len(t[1])>0 else -1
    box = hash_(label)
    boxes[box].append((label,operation_))
    
total_score=0
for box_ix, box in boxes.items():
    labels = OrderedDict()
    for item in box:
        if item[1]==-1:
            if item[0] in labels:
                labels.pop(item[0])
        else:
            labels.update({item[0]:item[1]})
            
    for label_ix, (_,focal_length) in enumerate(labels.items()):
        total_score+=(box_ix+1)*(label_ix+1)*focal_length

        
#print("pt1",total_)
print("pt2",total_score)
        