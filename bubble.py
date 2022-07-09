numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]
print(f'przed sortowaniem {numbers}')


def bubble_sort(numbers):
    change = 1
    while change > 0:
        change -= 1
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                change += 1
                numbers.insert(i, numbers[i + 1])
                numbers.pop(i + 2)
    return print(f'Po sortowaniu {numbers}')


def main():
    bubble_sort(numbers)


if __name__ == "__main__":
    main()
