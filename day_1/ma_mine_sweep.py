import pandas as pd


def get_input(prod=False):
    if prod:
        return pd.read_csv("input.txt", header=None)[0]
    else:
        return pd.Series([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])


if __name__ == "__main__":
    input_ = get_input(prod=True)
    diffed = input_.rolling(3).sum().diff().dropna()
    diffed = diffed[diffed > 0]
    print(diffed.count())