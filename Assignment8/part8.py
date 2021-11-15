def filter_even(*args):
    return list(filter(lambda x: not x % 2, args))


print(filter_even(1, 2, 3, 4, 5, 6, 7, 8, 9))
