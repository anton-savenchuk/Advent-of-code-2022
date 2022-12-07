def get_round(usr1: str, usr2: str) -> tuple:
    usr1_scores = usr2_scores = 0
    scores_for_shapes = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
    shapes_usr1 = ["A", "C", "B"]
    shapes_usr2 = ["X", "Z", "Y"]
    answer = ["a draw", "usr2", "usr1"]

    if answer[shapes_usr1.index(usr1) - shapes_usr2.index(usr2)] == "a draw":
        usr1_scores += 3 + scores_for_shapes[usr1]
        usr2_scores += 3 + scores_for_shapes[usr2]

    elif answer[shapes_usr1.index(usr1) - shapes_usr2.index(usr2)] == "usr1":
        usr1_scores += 6 + scores_for_shapes[usr1]
        usr2_scores += scores_for_shapes[usr2]

    else:
        usr1_scores += scores_for_shapes[usr1]
        usr2_scores += 6 + scores_for_shapes[usr2]

    return usr1_scores, usr2_scores


def get_shape(usr1: str, usr2: str) -> str:
    shape = ""
    if usr1 == "A":
        if usr2 == "X":
            shape = "Z"
        elif usr2 == "Z":
            shape = "Y"
        else:
            shape = "X"

    elif usr1 == "B":
        if usr2 == "X":
            shape = "X"
        elif usr2 == "Z":
            shape = "Z"
        else:
            shape = "Y"

    elif usr1 == "C":
        if usr2 == "X":
            shape = "Y"
        elif usr2 == "Z":
            shape = "X"
        else:
            shape = "Z"

    return shape


with open("input/day_02.txt", "r", encoding="utf-8") as file:
    elf_counter = my_counter = 0
    for row in file:
        elf_shape, my_shape = row.strip().split()
        elf, me = get_round(elf_shape, get_shape(elf_shape, my_shape))

        elf_counter += elf
        my_counter += me

print(my_counter)
