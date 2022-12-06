lst = [[]]
with open("input/day_01.txt", "r", encoding="utf-8") as file:
    for row in file:
        if row == "\n":
            lst.append([])
        else:
            lst[-1].append(int(row.strip()))

maximum = 0
for i in lst:
    _sum = sum(i)
    if _sum > maximum:
        maximum = _sum

print(maximum)
