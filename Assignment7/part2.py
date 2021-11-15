def far_to_cel(f):
    return (f-32)/9*5


def cel_to_far(c):
    return c/5*9+32


print(f'60C is {cel_to_far(60)} in Fahrenheit')
print(f"45C is {format(far_to_cel(45), '1.0f')} in Celsius")
