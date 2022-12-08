def get_move(move: str) -> None:
    _move, _from, _to = (int(i) for i in move.split() if i.isdigit())

    for _ in range(_move):
        stacks[_to - 1].append(stacks[_from - 1].pop(-1))


with open("input/day_05.txt", "r", encoding="utf-8") as file:

    _temp_stacks = []
    for row in file:
        if row == "\n":
            break
        # "    [D]    " -> ['', '[D]', '']
        _temp_stacks.append(row.replace("    ", " ").strip("\n").split(" "))

    _len = [int(i) for i in _temp_stacks[-1] if i.isdigit()][-1]
    stacks = [[] for _ in range(_len)]

    for row in _temp_stacks[: -1]:
        for key, elem in enumerate(row):
            if elem != "":
                stacks[key].insert(0, elem)

    for move in file:
        get_move(move)


for row in stacks:
    print(row[-1].strip("[]"), end="")
print()
