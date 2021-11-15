repetitions = 9

for i in range(1, repetitions + 1):
    output = ''
    for j in range(1, i + 1 if i < 6 else repetitions + 2 - i):
        output += '*'
    print(output)
