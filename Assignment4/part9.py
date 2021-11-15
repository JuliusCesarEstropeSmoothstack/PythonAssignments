# Question 1
output = ''
for x in range(2000, 3201):
    if (not x % 7) and x % 5:  # if number is multiple of 7 and not multiple of 5
        output += f'{x}, '
print(output[:-2])

# Question 2
factorial = 1
number = int(input('Enter number to factorialize'))

for x in range(1, number + 1):
    factorial *= x
print(factorial)

# Question 3
number = int(input('Enter an integral number'))
output = {i: {i * i} for i in range(1, number + 1)}  # Dictionary comprehension
print(output)

# Question 4
csn = list(str(input("Enter comma-separated numbers")).split(','))

print(csn)
print(tuple(csn))


# Question 5
class MyStringClass(object):

    def getString(self):
        return input('Enter a string please.')

    def printString(self, string: str):
        print(string.upper())


msc = MyStringClass()
msc.printString(msc.getString())
