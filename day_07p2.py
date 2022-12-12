MAX_FILESYSTEM_SIZE = 70_000_000
space_to_update = 30_000_000

dirs = {}
files = {}
paths = []


def get_path(name: str) -> str:
    return "/".join(paths) + "/" + name


with open("input/day_07.txt", "r", encoding="utf-8") as file:

    for row in file:
        if row.startswith("$ ls"):
            continue

        elif row.startswith("$ cd"):
            cd = row.strip().split()[-1]
            if cd == "/":
                paths = [""]
            elif cd == "..":
                paths.pop()
            else:
                paths.append(cd)

        elif row.startswith("dir"):
            _, dir_name = row.strip().split()
            dirs[get_path(dir_name)] = 0

        elif row.split()[0].isdigit():
            file_size, file_name = row.strip().split()
            files[get_path(file_name)] = int(file_size)


for dir_name in dirs:
    for key, value in files.items():
        if key.startswith(dir_name):
            dirs[dir_name] += value

total_files_size = sum(files.values())
max_files_size = MAX_FILESYSTEM_SIZE - space_to_update

for dir_size in sorted(dirs.values()):
    if total_files_size - dir_size <= max_files_size:
        print(dir_size)
        break
