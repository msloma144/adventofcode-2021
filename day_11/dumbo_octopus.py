import io
import time

import numpy as np

input_ = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


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

    file.close()
    return np.vstack(map_)


def get_surroundings(map_, loc):
    list_ = []
    for value in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        if 0 <= loc[0]+value[0] < map_.shape[0] and 0 <= loc[1]+value[1] < map_.shape[1]:
            list_.append((loc[0]+value[0], loc[1]+value[1]))
    return list_


def flash(loc):
    surroundings = get_surroundings(data, loc)

    for value in surroundings:
        data[value] += 1


if __name__ == "__main__":
    start_time = time.time()
    score_guide = {")": 3,
                   "]": 57,
                   "}": 1197,
                   ">": 25137}
    file = get_input(prod=True)
    IS_PART_2 = True
    total_flashes = 0
    data = read_file(file)
    iterations = 100

    if IS_PART_2:
        iterations = 1000

    for day in range(iterations):
        flashed_indexes = []
        data += 1
        done = False
        locs = np.where(data > 9)
        while not done:
            locs_bool = [True] * len(locs[0]) if len(locs) > 0 else []
            for index, (y, x) in enumerate(zip(*locs)):
                if (y, x) not in flashed_indexes:
                    total_flashes += 1
                    flash((y, x))
                    locs_bool[index] = False
                flashed_indexes.append((y, x))

            if sum(locs_bool) == len(locs_bool):
                done = True

            locs = np.where(data > 9)

        for value in flashed_indexes:
            data[value] = 0
        if IS_PART_2:
            if data.sum() == 0:
                print(f"synchronized on day: {day+1}")
                break

        print(f"Day: {day+1}")

    print(total_flashes)
    print(f"time: {time.time() - start_time}")





