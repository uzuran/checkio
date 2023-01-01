def correct_sentence(text: str) -> str:
    """
    returns a corrected sentence which starts with a capital letter
    and ends with a dot.
    """
    for i in text:
        if i == ".":
            return text[0].capitalize() + text[1:]
    else:
        return text[0].capitalize() + text[1:] + '.'

print(correct_sentence("welcome"))


# text = "small"
#
# capital = text.capitalize()
#
# print(capital)

