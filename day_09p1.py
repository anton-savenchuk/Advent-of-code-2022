head: list = [0, 0]
tail: list = [0, 0]
steps: set = {tuple(tail)}

with open("input/day_09.txt", "r", encoding="utf-8") as file:
    for row in file:

        route, step = row.split(" ")
        for _ in range(int(step)):
            if route == "U":
                head[0] -= 1
            elif route == "D":
                head[0] += 1
            elif route == "L":
                head[1] -= 1
            elif route == "R":
                head[1] += 1

            while any(abs(head[i] - tail[i]) > 1 for i in (0, 1)):
                for j in (0, 1):
                    tail[j] += (tail[j] < head[j]) - (head[j] < tail[j])
            steps.add(tuple(tail))

print(len(steps))
