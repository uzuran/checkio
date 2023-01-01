def sum_numbers(text: str) -> int:
    split_text = text.split()
    for i in split_text:
        numbers = [int(s) for s in split_text if s.isdigit()]
        if i.isdigit():
            return sum(numbers)

    return 0


print(sum_numbers(""))

