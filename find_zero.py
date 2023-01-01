def end_zeros(num: int) -> int:
    # your code here
    numstr = str(num)
    numstr = numstr[::-1]

    count = 0
    for i in numstr:
        if i == '0':
            count += 1
        else:
            break
    return count


print("Example:")
print(end_zeros(1000))
