def both_same_first(first_string: str, second_string: str):
    return first_string.lower()[0] == second_string.lower()[0]


print(both_same_first('Hello', 'howdy'))
print(both_same_first('goodbye', 'okay'))
