import io
import time

input_ = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def get_input(prod=False):
    if prod:
        return open("input.txt", "r")
    else:
        return io.StringIO(input_)


def generate_range(value1, value2):
    if value1 < value2:
        return range(value1, value2+1)
    else:
        return range(value2, value1+1)


def generate_diags(point_1, point_2):
    if point_1[0] > point_2[0]:
        x_values = generate_range(point_1[0], point_2[0])
    else:
        x_values = reversed(generate_range(point_1[0], point_2[0]))

    if point_1[1] > point_2[1]:
        y_values = generate_range(point_1[1], point_2[1])
    else:
        y_values = reversed(generate_range(point_1[1], point_2[1]))

    return list(x_values), list(y_values)


if __name__ == "__main__":
    PART_1 = False
    start_time = time.time()
    indexes = {}
    total_over_one = 0
    file = get_input(prod=True)
    first_line = True
    while True:
        line = file.readline()

        if not line:
            break
        line = line.strip()
        set_1, _, set_2 = line.split()
        set_1 = [int(item) for item in set_1.split(",")]
        set_2 = [int(item) for item in set_2.split(",")]

        hor_split = set_2[0] - set_1[0]
        vert_split = set_2[1] - set_1[1]

        keys = []
        if vert_split == 0:
            values = generate_range(set_1[0], set_2[0])
            keys = [f"{value}, {set_1[1]}" for value in values]

        elif hor_split == 0:
            values = generate_range(set_1[1], set_2[1])
            keys = [f"{set_1[0]}, {value}" for value in values]

        else:
            if not PART_1:
                x_values, y_values = generate_diags(set_1, set_2)
                keys = [f"{x_values[index]}, {y_values[index]}" for index in range(len(x_values))]

        for key in keys:
            key_val = indexes.get(key, None)
            if key_val is None:
                indexes[key] = 1
            else:
                indexes[key] += 1
                if indexes[key] == 2:
                    total_over_one += 1

    file.close()
    print(total_over_one)
    print(f"Time (s): {time.time() - start_time}")