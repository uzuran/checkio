def beginning_zeros(a: str) -> int:
    count = 0
    while True:
        for i in a:
            if i == "0":
                count += 1
            else:
                break
        return count



print(beginning_zeros("0100"))
