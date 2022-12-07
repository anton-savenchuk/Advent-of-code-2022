with open("input/day_03.txt", "r", encoding="utf-8") as rucksacks:

    priority_list = []
    for rucksack in rucksacks:
        first_compartment = rucksack.strip()[:len(rucksack)//2]
        second_compartment = rucksack.strip()[len(rucksack)//2:]

        joint_item = "".join(set(first_compartment) & set(second_compartment))

        priority_list.append(
            ord(joint_item) - (96 if joint_item.islower() else 38)
        )

print(sum(priority_list))
