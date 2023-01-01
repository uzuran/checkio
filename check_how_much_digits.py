from typing import List


def count_digits(text: str) -> int:
    split_text = text.split()
    count = 0
    while True:
        for i in split_text:
            for j in i:
                if j.isdigit():
                    count += 1
        return count





print(count_digits("who is 1st here"))