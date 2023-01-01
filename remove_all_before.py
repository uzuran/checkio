from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:

    if border not in items:
        return items
    position = items.index(border)
    return items[position:]


print(list(remove_all_before([5, 1, 2, 3, 4, 5], 2)))
