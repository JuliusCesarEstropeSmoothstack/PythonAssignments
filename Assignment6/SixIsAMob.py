names = ['Tom', 'John', 'Anne', 'Suzie', 'Luanne', 'Michael']


def crowd_test(name_list):
    if len(name_list > 5):
        print("There's a mob in here!")
    elif len(name_list) > 3:
        print('Crowded.')
    elif len(name_list) == 0:
        print('The room is empty.')
    else:
        print('The room is not crowded.')


crowd_test(names)

names.remove('Tom')
crowd_test(names)
