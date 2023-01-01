def is_all_upper(text: str) -> bool:
    replace_text = text.replace(" ", "")

    if replace_text.islower():
        return False
    if replace_text.isupper():
        return True
    if replace_text.isdigit():
        return True
    if replace_text == "":
        return True
    else:
        return False



print(is_all_upper("55 55 5 "))






