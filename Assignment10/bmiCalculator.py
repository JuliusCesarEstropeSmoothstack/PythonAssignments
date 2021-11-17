data_points = int(input('Enter the number of data points:'))
answers = ''


def calc_bmi(weight: float, height: float):
    return weight / height ** 2


def evaluate_bmi(bmi: float):
    if bmi < 18.5:
        return 'under'
    if bmi < 25:
        return 'normal'
    if bmi < 30:
        return 'over'
    return 'obese'


for x in range(data_points):
    # Convert the input data into strings and split for use later
    data_point = list(map(lambda y: float(y), input(f'Enter data point {x + 1}').split()))
    calced_bmi = calc_bmi(data_point[0], data_point[1])
    answers += evaluate_bmi(calced_bmi) + ' '

print(f'Answer: {answers[:-1]}')
