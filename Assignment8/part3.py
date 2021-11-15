def func3(x, y, z):
    return x if z else y


print(func3(1, 2, True))
print(func3(1, 2, False))
