import time


def get_input(prod=False):
    if prod:
        return [4,1,4,1,3,3,1,4,3,3,2,1,1,3,5,1,3,5,2,5,1,5,5,1,3,2,5,3,1,3,4,2,3,2,3,3,2,1,5,4,1,1,1,2,1,4,4,4,2,1,2,1,5,1,5,1,2,1,4,4,5,3,3,4,1,4,4,2,1,4,4,3,5,2,5,4,1,5,1,1,1,4,5,3,4,3,4,2,2,2,2,4,5,3,5,2,4,2,3,4,1,4,4,1,4,5,3,4,2,2,2,4,3,3,3,3,4,2,1,2,5,5,3,2,3,5,5,5,4,4,5,5,4,3,4,1,5,1,3,4,4,1,3,1,3,1,1,2,4,5,3,1,2,4,3,3,5,4,4,5,4,1,3,1,1,4,4,4,4,3,4,3,1,4,5,1,2,4,3,5,1,1,2,1,1,5,4,2,1,5,4,5,2,4,4,1,5,2,2,5,3,3,2,3,1,5,5,5,4,3,1,1,5,1,4,5,2,1,3,1,2,4,4,1,1,2,5,3,1,5,2,4,5,1,2,3,1,2,2,1,2,2,1,4,1,3,4,2,1,1,5,4,1,5,4,4,3,1,3,3,1,1,3,3,4,2,3,4,2,3,1,4,1,5,3,1,1,5,3,2,3,5,1,3,1,1,3,5,1,5,1,1,3,1,1,1,1,3,3,1]
    else:
        return [3,4,3,1,2]


if __name__ == "__main__":
    start_time = time.time()
    arr = get_input(prod=True)
    NUM_DAYS = 256
    rev_list = list(reversed(range(9)))

    nums_ = [0] * 9
    for value in arr:
        nums_[value] += 1

    for days in range(NUM_DAYS):
        new_nums = [0] * 9
        for index in rev_list:
            if nums_[index] > 0:
                if index == 0:
                    new_nums[8] += 1 * nums_[index]
                    new_nums[6] += nums_[index]
                if index - 1 >= 0:
                    new_nums[index - 1] = nums_[index]

        nums_ = new_nums

    print(sum(nums_))
    print(f"time: {time.time() - start_time}")

