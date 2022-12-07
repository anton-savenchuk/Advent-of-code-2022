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


with open("input/day_02.txt", "r", encoding="utf-8") as file:
    elf_counter = my_counter = 0
    for row in file:
        elf, me = get_round(*row.strip().split())
        elf_counter += elf
        my_counter += me

print(my_counter)
