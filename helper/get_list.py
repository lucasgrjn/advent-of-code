import re

from pathlib import Path


# find_nums = lambda l: re.match(r'(\d+)', l)
find_nums = re.compile(r'(\d+)')


def get_numbers(fpath: Path) -> list[list[int]]:
    data = []
    with open(fpath, "rt") as f:
        lines = f.readlines()
        for ll in lines:
            data.append(list(map(int, find_nums.findall(ll))))
    return data