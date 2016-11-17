import re


def is_valid_postal(postal):  # difficulty-level: hard
    base_regex = re.compile(r'^[1-9][0-9]{5}$')
    alter_regex = re.compile(r'([0-9])([0-9])(?=\1)')
    alter_matches = []

    for i in range(5):
        alter_matches += [bool(alter_regex.match(postal[i:]))]

    return sum(alter_matches) < 2 and bool(base_regex.match(postal))


print(is_valid_postal(str(input())))