names = ['Tom', 'John', 'Anne', 'Suzie']


def crowd_test(name_list):
    if len(name_list) > 3:
        print('Crowded.')


crowd_test(names)

names.remove('Tom')
crowd_test(names)
