def is_even(num: int) -> bool:
    check_even = num % 2
    if check_even == 0:

        return True
    else:

        return False


print(is_even(7))


def is_even(num: int) -> bool:
    return num & 1 == 0


print(is_even(7))
