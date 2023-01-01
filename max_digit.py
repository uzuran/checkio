def max_digit(value: int) -> int:
    if value:
        str_value = str(value)
        max_value = max(str_value)
        return int(max_value)

    else:
        return 0


print(max_digit(52))