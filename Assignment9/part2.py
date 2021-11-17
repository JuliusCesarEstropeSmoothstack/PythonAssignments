nested_list = [[34587, 98762, 77226, 88112], [4, 5, 3, 3], [40.95, 56.80, 32.95, 24.99]]

order_numbers = nested_list[0]
quantities = nested_list[1]
prices_per_item = nested_list[2]

# Increases quantity by 10 if the price per item is less than 100
quantity_price = list(map(lambda x, y: f'{x if y > 100 else x + 10} * {y}', quantities, prices_per_item))

# print(quantity_price)

account_book = list(map(lambda x, y: (x, y), order_numbers, quantity_price))

print(account_book)
