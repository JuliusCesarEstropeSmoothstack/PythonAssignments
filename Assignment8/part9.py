def even_capital_case(input_string):
    new_string = ''
    count = 0
    for character in input_string:
        if not count % 2:
            new_string += str(character).upper()
        else:
            new_string += str(character).lower()

        count += 1
    return new_string


print(even_capital_case('hoWDY theRE'))
