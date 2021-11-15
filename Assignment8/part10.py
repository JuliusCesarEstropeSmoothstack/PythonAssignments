def comparison_function(num1, num2):
    if num1 % 2 or num2 % 2:
        return num1 if num1 > num2 else num2
    else:
        return num1 if num1 < num2 else num2


print(comparison_function(2, 4))
print(comparison_function(1, 4))
