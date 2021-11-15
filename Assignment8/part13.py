def cap_first_fourth(input_string: str):
    new_string = list(x for x in input_string)
    if len(new_string) > 0:
        new_string[0] = str(new_string[0]).upper()
    if len(new_string) > 3:
        new_string[3] = str(new_string[3]).upper()
    return ''.join(new_string)


print(cap_first_fourth(''))
print(cap_first_fourth('how'))
print(cap_first_fourth('howdy there'))
