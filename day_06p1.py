def get_marker_id(string: str) -> int:
    for i in range(len(string)):
        if len(set(string[i: i + 4])) == 4:
            return i + 4

with open("input/day_06.txt", "r", encoding="utf-8") as file:
    for row in file:
        marker_id = get_marker_id(row.strip())

print(marker_id)
