nested_list = [[34587, (1, 1, 40.95), (2, 1, 56.80), (3, 1, 32.85), (4, 1, 24.99)],
               [98762, (1, 5, 40.95), (2, 2, 56.80)],
               [77226, (4, 2, 24.99)],
               [88112, (2, 2, 56.80), (3, 2, 32.85), (4, 3, 24.99)]]


def order_total(order: list):
    total = 0

    for item in order[1:]:
        total += item[1] * item[2]

    return order[0], total


# Map each list in nested_list to the order_total function
orders = list(map(lambda x: order_total(x), nested_list))

print(orders)
