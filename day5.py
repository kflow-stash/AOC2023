input_ = open("data/day5.txt", "r").read()
seeds = [int(i) for i in input_.splitlines()[0].split(": ")[1].split(" ")]

t = [x.split(":\n")[1].split("\n") for x in input_.split("\n\n")[1:]]
mappers = [x.split(":\n")[1].split("\n") for x in input_.split("\n\n")[1:]]

for ix, map_list in enumerate(mappers):
    mappers[ix] = [[int(x) for x in y.split(" ")] for y in map_list]
    mappers[ix] = {(x[1], x[1] + x[2]): x[0] - x[1] for x in mappers[ix]}


# finds intersection between two range tuples
def intersect_(a, b):
    if max(a[0], b[0]) < min(a[1], b[1]):
        return (max(a[0], b[0]), min(a[1], b[1]))


# gets source ranges that are not covered in the map input ranges
def get_uncovered(s_rng, a, b):
    rngs = []
    if s_rng[0] < a:
        rngs.append((s_rng[0], min(a, s_rng[1])))
    if s_rng[1] > b:
        rngs.append((max(b, s_rng[0]), s_rng[1]))
    return rngs


final_nodes = {}


# this is a recursive function that finds the "tree" paths for all range subsets
def sand_filter(map_ix, s_rng, delt):
    if map_ix == len(mappers):
        final_nodes[(s_rng[0] - delt, s_rng[1] - delt)] = delt
    else:
        for m_rng, m_delt in mappers[map_ix].items():
            inter = intersect_(s_rng, m_rng)
            if inter:
                sand_filter(map_ix + 1, [x + m_delt for x in inter], m_delt + delt)

        uncovered_ranges = get_uncovered(
            s_rng,
            min([x[0] for x in mappers[map_ix].keys()]),
            max([x[1] for x in mappers[map_ix].keys()]),
        )
        for rng in uncovered_ranges:
            sand_filter(map_ix + 1, rng, delt)


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


seeds2 = [(x, x + y) for x, y in divide_chunks(seeds, 2)]

sand_filter(0, (0, max([x[1] for x in seeds2])), 0)

seed_mins = []
for seed in seeds2:
    mins = []
    for rng, delt in final_nodes.items():
        inter = intersect_(seed, rng)
        if inter:
            mins.append(inter[0] + delt)

    seed_mins.append(min(mins))

print("pt2", min(seed_mins))
