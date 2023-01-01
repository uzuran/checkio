def easy_unpack(elements: tuple) -> tuple:
    tuple_elements1 = elements[0]
    tuple_elements3 = elements[2]
    tuple_elements_second_last = elements[-2]
    return tuple_elements1, tuple_elements3, tuple_elements_second_last


print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))