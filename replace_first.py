from typing import Iterable


# def replace_first(items: list) -> Iterable:
#     first_object = items[0]
#     items.append(first_object)
#     items.remove(first_object)
#     return items
#
# print(replace_first([5]))


def replace_first(items: list) -> Iterable:
    if items:
        first_object = items[0]
        items.append(first_object)
        items.remove(first_object)
        return items
    else:
        return []

print(replace_first([1, 2, 3, 4]))




