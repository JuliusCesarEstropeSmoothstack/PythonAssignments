numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

evenCount = 0
oddCount = 0

for number in numbers:
    if number % 2:  # False if the number is even, True if odd
        print(number)
        oddCount += 1
    else:
        evenCount += 1

print(f'Number of even numbers: {evenCount}')
print(f'Number of odd numbers: {oddCount}')
