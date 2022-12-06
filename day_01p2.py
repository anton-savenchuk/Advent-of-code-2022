lst = [[]]
with open("input/day_01.txt", "r", encoding="utf-8") as file:
    for row in file:
        if row == "\n":
            lst.append([])
        else:
            lst[-1].append(int(row.strip()))

sums_calories = [sum(i) for i in lst]
top_three_elves = sorted(sums_calories)[-3:]

print(sum(top_three_elves))
