from collections import Counter

with open("input/day_04.txt", "r", encoding="utf-8") as camp:

    common_section_counter = 0
    for section in camp:

        pairs = section.strip().split(",")
        section1_indexes = list(map(int, pairs[0].split("-")))
        section2_indexes = list(map(int, pairs[1].split("-")))

        section1 = list(range(section1_indexes[0], section1_indexes[1] + 1))
        section2 = list(range(section2_indexes[0], section2_indexes[1] + 1))

        common_sections = list((Counter(section1) & Counter(section2)).elements())

        if common_sections in (section1, section2):
            common_section_counter += 1

print(common_section_counter)
