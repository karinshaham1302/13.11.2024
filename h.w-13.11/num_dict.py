power_of_tree: dict[int, int] = {
    1: 1 ** 3,
    2: 2 ** 3,
    3: 3 ** 3,
    4: 4 ** 3,
    5: 5 ** 3,
    6: 6 ** 3,
    7: 7 ** 3,
    8: 8 ** 3,
    9: 9 ** 3,
    10: 10 ** 3
}

number: int = int(input('Enter a number:'))
print(power_of_tree.get(number, 'invalid number'))
