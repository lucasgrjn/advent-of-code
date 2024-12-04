from pathlib import Path

from helper.get_list import get_numbers


# fdata = Path("./2024/data/day_01_test.txt")
fdata = Path("./2024/data/day_01_input.txt")
numbers = get_numbers(fdata)

# Using map
list_A_og = list(map(lambda x: x[0], numbers))
list_B_og = list(map(lambda x: x[1], numbers))

list_A = sorted(list_A_og)
list_B = sorted(list_B_og)

result1 = map(lambda x, y: abs(y - x), list_A, list_B)
print(f"Results - part 1: {sum(result1)}")

result2 = map(lambda x, y: x * list_B.count(x), list_A_og, list_B_og)
print(f"Results - part 2: {sum(result2)}")
