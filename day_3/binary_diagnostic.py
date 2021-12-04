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
        return open("input.txt", "r")
    else:
        return io.StringIO(input_)

start_time = time.time()
ones = []
zeros = []

file = get_input(prod=True)

first_line = True
while True:
    line = file.readline()

    if not line:
        break
    line = line.strip()

    if first_line:
        first_line = False
        ones = [0] * len(line)
        zeros = [0] * len(line)

    for index, value in enumerate(line):
        if value == "0":
            zeros[index] += 1
        elif value == "1":
            ones[index] += 1
        else:
            raise ValueError("Not a binary value!")

file.close()

gamma = ""
epsilon = ""
for index in range(len(ones)):
    if ones[index] > zeros[index]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)
print(time.time() - start_time)
