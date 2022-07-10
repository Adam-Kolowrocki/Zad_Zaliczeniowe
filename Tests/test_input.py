import random
from random import randint


def data_input():
    source_choice = 'k'
    if source_choice == 'f':
        with open('../n_numbers.txt') as f:
            numbers = f.readline()
            numbers = numbers.rsplit(", ")
            for i in range(0, len(numbers)):
                numbers[i] = int(numbers[i])
            return numbers
    elif source_choice == 'r':
        numbers = []
        for i in range(0, 30):
            n = random.randint(10, 99)
            numbers.append(n)
        return numbers
    elif source_choice == 'k':
        while True:
            numbers = []
            num_count = int(input(f'How many natural numbers do You want to sort ?'))
            if num_count <= 0:
                print(f'Wrong number... Type natural number.')
                continue
            for i in range(1, num_count + 1):
                user_input = int(input(f'Type {i} number ->'))
                if user_input > 0:
                    numbers.append(user_input)
                else:
                    print(f'Wrong number... Type natural numbers.')
            return numbers


data_input()
