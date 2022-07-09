first = [12, 23, 45]
second = [23, 45, 67]
third = first + second
print(third)
numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]
print(numbers)
print(len(numbers))


def merge(numbers):
    if len(numbers) > 1:
        left_numbers = numbers[:len(numbers) // 2]
        right_numbers = numbers[len(numbers) // 2:]
        print(left_numbers)
        print(right_numbers)

        merge(left_numbers)
        merge(right_numbers)


merge(numbers)
