def most_frequent(data: list[str]) -> str:
    most_freq = (max(set(data), key=data.count))

    return most_freq


print("Example:")

print(most_frequent(["a", "b", "c", "a", "b", "a"]))
