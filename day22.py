import itertools as iter
input_ = open("data/day22.txt", "r").read().splitlines()

class Block():

    def __init__(self,coords,ix):
        self.block_ix = ix
        self.initial_height = min(coords[0][2],coords[1][2])
        self.resting_height = -1
        self.xy_coords = [(coords[0][0],coords[0][1]),(coords[1][0],coords[1][1])]
        self.length = max(coords[0][2],coords[1][2])-min(coords[0][2],coords[1][2])
        self.topz = 0 
        self.xy_points = self.get_xy_points()
        self.supporting = []
        self.supported_by = []
        self.supported_chain = set()

    def __repr__(self):
        return f"""block {self.block_ix}. x,y: {self.xy_coords}. initial_height: {self.initial_height}. resting_height: {self.resting_height} topz: {self.topz} supporting: {", ".join([str(x.block_ix) for x in self.supporting])}. supported by: {", ".join([str(x.block_ix) for x in self.supported_by])} \n"""
    
    def get_xy_points(self):
        x_ends = (self.xy_coords[0][0],self.xy_coords[1][0])
        xs = list(range(min(x_ends),max(x_ends)+1))
        y_ends = (self.xy_coords[0][1],self.xy_coords[1][1])
        ys = list(range(min(y_ends),max(y_ends)+1))
        if len(xs)==1:
            return set(zip(iter.repeat(xs[0]),ys))
        elif len(ys) == 1:
            return set(zip(xs,iter.repeat(ys[0])))
        else:
            return set(zip(xs,ys))

        
blocks = []
for ix,block in enumerate(input_):
    blocks.append(Block([tuple(int(y) for y in x.split(",")) for x in block.split("~")],ix))
    
sorted_blocks = sorted(blocks,key=lambda x: x.initial_height)

for init_height, block_group in iter.groupby(sorted_blocks,lambda x: x.initial_height):
    blocks_below = list(sorted(filter(lambda x: x.resting_height>0 and x.resting_height + x.length<init_height,sorted_blocks),key =lambda x: x.resting_height + x.length,reverse=True))
    for block in block_group:
        s_chain = set()
        for below in blocks_below:
            if (
                below.block_ix != block.block_ix
                    and
                below.topz>= block.resting_height-1
                    and
                len(block.xy_points.intersection(below.xy_points)) > 0):
                
                if len(s_chain) > 0:
                    s_chain = s_chain.intersection(below.supported_chain)
                else:
                    s_chain = below.supported_chain
                
                block.resting_height = below.topz+1
                block.topz = block.length + block.resting_height
                below.supporting.append(block)
                block.supported_by.append(below)
        if len(block.supported_by)==1:
            block.supported_chain = block.supported_by[0].supported_chain.union({block.supported_by[0].block_ix})
        else:
            block.supported_chain = s_chain

        if block.resting_height == -1:
            block.resting_height = 1
            block.topz = block.resting_height + block.length
            

can_be_removed = set()
for block in sorted_blocks:
    if len(block.supporting) == 0:
        can_be_removed.add(block.block_ix)
    else:
        for supported_ in block.supporting:
            if len(supported_.supported_by) == 1:
                break
        else:
            can_be_removed.add(block.block_ix)

print(len(can_be_removed))
stop_here = 1

fall = 0
for block in sorted_blocks:
    if block.block_ix not in can_be_removed:
        for block2 in sorted_blocks:
            if block.block_ix in block2.supported_chain:
                fall+=1

                
print("pt2",fall)