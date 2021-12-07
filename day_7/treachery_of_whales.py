import numpy as np
import math
import time

input_ = [16,1,2,0,4,2,7,1,2,14]


def get_input(prod=False):
    if prod:
        return open("input.txt", "r").readline().strip().split(",")
    else:
        return input_


def test_sum(deltas):
    sum_ = 0
    for value in deltas:
        for _ in range(int(value) + 1):
            sum_ += _
    return sum_


if __name__ == "__main__":
    start_time = time.time()
    IS_PART_2 = True
    data = get_input(prod=True)
    data = np.array(data, dtype=np.int)

    if IS_PART_2:
        mean = math.floor(np.mean(data))
        deltas = np.abs(data - mean)
        sum_1 = test_sum(deltas)

        mean = math.ceil(np.mean(data))
        deltas = np.abs(data - mean)
        sum_2 = test_sum(deltas)
        if sum_1 < sum_2:
            sum_ = sum_1
        else:
            sum_ = sum_2
    else:
        deltas = np.abs(data - np.median(data))
        sum_ = np.sum(np.abs(data - deltas))

    print(sum_)
    print(f"time: {time.time() - start_time}")
