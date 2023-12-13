import itertools as iter
import re

input_ = open("data/day12.txt", "r").read().splitlines()


springs = []
groups = []
for row_ in input_:
    s, g = row_.split(" ")
    s = "?".join([s for x in range(5)])
    g = ",".join([g for x in range(5)])
    springs.append(s)
    groups.append([int(x) for ix, x in enumerate(g.split(","))])


def match_spring(group, spring):
    if len(spring) < len(group):
        return False

    for x, y in zip(spring, group):
        if x == "." and y != ".":
            return False
        elif x == "#" and y == ".":
            return False
    return True


def damage_full(ix, end_ix, chunk):
    chunk_damage = set(range(ix, ix + len([x for x in chunk if x == "#"])))

    dl = {x for x in damage_locs if x >= ix and x < end_ix}
    if dl.intersection(chunk_damage) == dl or len(dl) == 0:
        return True
    else:
        return False


def snap_in_right(chunk_ix, end_ix, built_map):
    if chunk_ix == len(sorted_chunks):
        final_map = "".join(["." for _ in range(end_ix)]) + built_map
        if match_spring(final_map,spring):
            return 1
        else:
            return 0

    (chunk_str, start_ix) = sorted_chunks[chunk_ix]
    match_count = 0

    for ix in range(start_ix, end_ix):
        if (
            ix not in locks
            and match_spring(chunk_str, spring[ix:end_ix])
            and damage_full(ix, end_ix, chunk_str)
        ):
            if (chunk_ix,ix) in chunk_cache.keys():
                match_count = chunk_cache[(chunk_ix,ix)]
            else:

                match_count += snap_in_right(
                    chunk_ix + 1,
                    ix,
                    chunk_str
                    + "".join(["." for _ in range(ix + len(chunk_str), end_ix)])
                    + built_map,
                )
                chunk_cache[(chunk_ix,ix)] = match_count  

    return match_count


sum_ = 0
for loop_ix, (group, spring) in enumerate(zip(groups, springs)):

    total_maps = []
    chunk_cache = {}

    damages = list(
        set([(x, len(x)) for x in spring.replace("?", ".").split(".") if len(x) > 0])
    )

    locks = set()
    for x, y in damages:
        locks = locks.union(
            set(
                [
                    n
                    for m in re.finditer(x, spring)
                    for n in range(m.start() + 1, m.start() + y + 1)
                ]
            )
        )

    damage_locs = set([x for x, y in enumerate(spring) if y == "#"])

    group_chunks = ["".join(list(iter.repeat("#", x)) + ["."]) for x in group]
    group_chunks[-1] = group_chunks[-1][:-1]

    sorted_chunks = list(reversed(list(
        zip(group_chunks, [0] + list(iter.accumulate([len(x) for x in group_chunks])))
    )))

    # snap in right chunk by chunk
    match_count = snap_in_right(0, len(spring), "")


    print(loop_ix, match_count)

    sum_ += match_count

print("pt2", sum_)
