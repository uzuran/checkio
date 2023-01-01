# Python program for implementation of Bubble Sort


def bubble(lst):
    lst_index = len(lst) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, lst_index):
            if lst[i] > lst[i+1]:
                sorted = False
                lst[i], lst[i+1] = lst[i+1], lst[i]

    return lst


print(bubble([1, 8, 6, 5, 2, 6]))