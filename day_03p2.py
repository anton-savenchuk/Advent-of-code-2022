with open("input/day_03.txt", "r", encoding="utf-8") as rucksacks:

    priority_list = []

    groups = [[]]
    for rucksack in rucksacks:
        if len(groups[-1]) >= 3:
            groups.append([])
        groups[-1].append(rucksack.strip())

    for group in groups:
        joint_group_item = "".join(
            set(group[0]) & set(group[1]) & set(group[2])
        )

        priority_list.append(
            ord(joint_group_item) - (
                96 if joint_group_item.islower() else 38
            )
        )

print(sum(priority_list))
