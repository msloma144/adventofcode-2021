import io

input_ = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def get_input(prod=False):
    if prod:
        return open("input.txt", "r")
    else:
        return io.StringIO(input_)


vertical = 0
horizontal = 0

file = get_input(prod=True)

while True:
    line = file.readline()

    if not line:
        break

    dir_, amt = line.split()

    amt = int(amt)
    if dir_ == "forward":
        horizontal += amt
    elif dir_ == "down":
        vertical += amt
    elif dir_ == "up":
        vertical -= amt
    else:
        raise ValueError("Direction is not valid!")

file.close()

print(vertical * horizontal)
