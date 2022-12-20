rope: list = [[0, 0] for _ in range(10)]
steps: set = {tuple(rope[-1])}

with open("input/day_09.txt", "r", encoding="utf-8") as file:
    for row in file:

        route, step = row.split(" ")
        for _ in range(int(step)):
            if route == "D":
                rope[0][1] -= 1
            elif route == "L":
                rope[0][0] -= 1
            elif route == "R":
                rope[0][0] += 1
            elif route == "U":
                rope[0][1] += 1

            for prev, cur in zip(rope, rope[1:]):
                while any(abs(cur[j] - prev[j]) > 1 for j in (0, 1)):
                    for j in (0, 1):
                        cur[j] += (cur[j] < prev[j]) - (prev[j] < cur[j])
            steps.add(tuple(rope[-1]))

print(len(steps))
