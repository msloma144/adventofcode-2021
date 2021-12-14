import io
import time
from collections import Counter
import numpy as np

input_ = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

def get_input(prod=False):
    if prod:
        return open("input.txt", "r")
    else:
        return io.StringIO(input_)


def read_file(file):
    folds = []
    indexes = []
    max_x = 0
    max_y = 0
    for line in file.readlines():
        line = line.strip()
        if line != "":
            if "fold" not in line:
                x, y = line.split(",")
                x = int(x)
                y = int(y)

                if max_x < x:
                    max_x = x
                if max_y < y:
                    max_y = y
                indexes.append((y, x))
            else:
                axis = line[11:12]
                value = int(line[13:])
                folds.append((axis, value))

    arr = np.zeros((max_y+1, max_x+1))
    for (y, x) in indexes:
        arr[y, x] = 1

    return arr, folds

def fold_x(at_x):
    right = arr[:, :at_x]
    left = arr[:, at_x+1:]

    left_flipped = np.flip(left, axis=1)
    if left_flipped.shape[1] != right.shape[1]:
        left_flipped = np.hstack([left_flipped.shape[0], np.zeros((right.shape[1] - left_flipped.shape[1])), left_flipped])
    right += left_flipped
    return right

def fold_y(at_y):
    upper = arr[:at_y]
    lower = arr[at_y+1:]

    lower_flipped = np.flip(lower, axis=0)
    if lower_flipped.shape[0] != upper.shape[0]:
        lower_flipped = np.vstack([np.zeros((upper.shape[0] - lower_flipped.shape[0], lower_flipped.shape[1])), lower_flipped])
    upper += lower_flipped
    return upper

if __name__ == "__main__":
    start_time = time.time()
    file = get_input(prod=True)
    IS_PART_2 = True
    arr, folds = read_file(file)
    for (axis, value) in folds:
        if axis == "y":
            arr = fold_y(value)
        else:
            arr = fold_x(value)
        print(arr)
        print(np.count_nonzero(arr > 0))

    arr[arr > 1] = 1
    for line in arr:
        print(list(line))
    print(f"time: {time.time() - start_time}")





