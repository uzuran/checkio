from typing import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    empty_list = []
    for i in donuts:
        empty_list.append(i)
        if i == 0:
            empty_list.append(i)
    return empty_list


print(duplicate_zeros([0, 2, 3, 0, 4, 0]))