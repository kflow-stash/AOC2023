import itertools as iter

input_ = open("data/day13.txt", "r").read().replace("#", "1").replace(".", "0").split("\n\n")

grids = []
for grid in input_:
    grid = [[int(y) for y in x] for x in grid.split("\n")]
    grid_dict = {"rows": [tuple(x) for x in grid]}
    grid_dict["cols"] = list(map(tuple, zip(*grid)))
    grids.append(grid_dict)


def lazy_compare(a, b, part1=True):
    for diff in iter.accumulate(
        abs(x - y)
        for x, y in zip(
            iter.chain.from_iterable(a),
            iter.chain.from_iterable(b),
        )
    ):
        if part1 and diff > 0:
            return False
        if diff > 1:
            return False
    if part1 and diff == 0:
        return True
    elif diff == 1:
        return True
    else:
        return False


part1 = True
total_ = 0
for grid in grids:
    rows, cols = (
        grid["rows"],
        grid["cols"],
    )
    for ix in range(1, len(rows) // 2 + 1):
        if lazy_compare(rows[:ix], reversed(rows[ix : (ix * 2)]), part1):
            total_ += ix * 100
            break

        if lazy_compare(rows[-ix:], reversed(rows[-(ix * 2) : -ix]), part1):
            total_ += (len(rows) - ix) * 100
            break

    for jx in range(1, len(cols) // 2 + 1):
        if lazy_compare(cols[:jx], reversed(cols[jx : (jx * 2)]), part1):
            total_ += jx
            break

        if lazy_compare(cols[-jx:], reversed(cols[-(jx * 2) : -jx]), part1):
            total_ += len(cols) - jx
            break


if part1:
    print("pt1", total_)
else:
    print("pt2", total_)