import io
import time

input_ = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def get_input(prod=False):
    if prod:
        return open("input.txt", "r").readlines()
    else:
        return io.StringIO(input_).readlines()


def recur(possible_values, bit_num, max_bits, sensor):
    if len(possible_values) == 1:
        return possible_values[0]

    ones_win = []
    zeros_win = []
    ones_count = 0
    zeros_count = 0

    if bit_num < max_bits:
        for line in possible_values:
            line = line.strip()

            value = line[bit_num]
            if value == "0":
                zeros_count += 1
                zeros_win.append(line)
            elif value == "1":
                ones_count += 1
                ones_win.append(line)
            else:
                raise ValueError("Not a binary value!")

        if ones_count >= zeros_count:
            if sensor == "o2_generator":
                return recur(ones_win, bit_num+1, max_bits, sensor)
            elif sensor == "scrubber":
                return recur(zeros_win, bit_num+1, max_bits, sensor)

        else:
            if sensor == "o2_generator":
                return recur(zeros_win, bit_num+1, max_bits, sensor)
            elif sensor == "scrubber":
                return recur(ones_win, bit_num+1, max_bits, sensor)
    else:
        return -1


start_time = time.time()
lines = get_input(prod=True)
num_bits = len(lines[0].strip())

o2_generator = recur(lines, 0, num_bits, sensor="o2_generator")
gamma = int(o2_generator, 2)
scrubber = recur(lines, 0, num_bits, sensor="scrubber")
epsilon = int(scrubber, 2)

print(gamma * epsilon)
print(time.time() - start_time)