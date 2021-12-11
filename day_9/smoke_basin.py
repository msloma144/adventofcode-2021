import io
import time

import numpy as np

input_ = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def get_input(prod=False):
    if prod:
        return open("input.txt", "r")
    else:
        return io.StringIO(input_)


def read_file(file):
    map_ = []

    while True:
        line = file.readline()
        if not line:
            break
        map_.append(np.array(list(line.strip()), dtype=int))

    return np.vstack(map_)


def is_min(map_, loc):
    my_value = map_[loc[0], loc[1]]
    if loc[0]+1 < map_.shape[0] and not my_value < map_[loc[0]+1, loc[1]]:
        return False
    if loc[1]+1 < map_.shape[1] and not my_value < map_[loc[0], loc[1]+1]:
        return False
    if loc[0]-1 >= 0 and not my_value < map_[loc[0]-1, loc[1]]:
        return False
    if loc[1]-1 >= 0 and not my_value < map_[loc[0], loc[1]-1]:
        return False
    return True


def get_surroundings(map_, loc):
    list_ = []
    if loc[0]+1 < map_.shape[0]:
        list_.append((loc[0]+1, loc[1]))
    if loc[1]+1 < map_.shape[1]:
        list_.append((loc[0], loc[1]+1))
    if loc[0]-1 >= 0:
        list_.append((loc[0]-1, loc[1]))
    if loc[1]-1 >= 0:
        list_.append((loc[0], loc[1]-1))
    return list_


def enumerate_basin(map_, loc):
    already_seen_indexes = [loc]
    still_to_enum = [loc]
    total = 1
    while len(still_to_enum) != 0:
        loc_ = still_to_enum.pop(0)
        surroundings = get_surroundings(map_, loc_)
        to_remove = []
        for index, value in enumerate(surroundings):
            if map_[value] == 9:
                to_remove.append(index)
            if value in already_seen_indexes:
                to_remove.append(index)

        for index in reversed(to_remove):
            del surroundings[index]

        already_seen_indexes += surroundings

        total += len(surroundings)
        still_to_enum += surroundings

    return total


if __name__ == "__main__":
    start_time = time.time()
    min_indexes = []
    min_values = []

    file = get_input(prod=True)
    map_ = read_file(file)

    for y in range(map_.shape[0]):
        for x in range(map_.shape[1]):
            if is_min(map_, (y, x)):
                min_indexes.append((y, x))
                min_values.append(map_[y, x])

    print(sum(min_values) + len(min_values))

    sizes = []
    for loc in min_indexes:
        sizes.append(enumerate_basin(map_, loc))

    total = 1
    for value in sorted(sizes)[-3:]:
        total *= value
    print(total)