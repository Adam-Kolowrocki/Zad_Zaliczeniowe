def heap(numbers, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and numbers[i] < numbers[l]:
        largest = l

    if r < n and numbers[largest] < numbers[r]:
        largest = r

    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]

        heap(numbers, n, largest)


def heap_sort(numbers):
    n = len(numbers)

    for i in range(n // 2 - 1, -1, -1):
        heap(numbers, n, i)

    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heap(numbers, i, 0)
    return numbers


def reverse(numbers):
    numbers = heap_sort(numbers)
    print(numbers)
    descending = numbers.reverse()
    return descending

numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]


def main():
    print(numbers)
    print(reverse(numbers))


if __name__ == "__main__":
    main()
