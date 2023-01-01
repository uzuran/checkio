from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:

    for i in elements:
        if elements[0] != i:
            return False
    else:
        return True



print(all_the_same([1, 1, 1, 1]))
