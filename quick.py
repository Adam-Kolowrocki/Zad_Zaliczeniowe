numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]


def partitioning(numbers, start, end):
    pivot = numbers[start]
    left = start + 1
    right = end

    while True:
        while left <= right and numbers[right] >= pivot:
            right -= 1
        while left <= right and numbers[left] <= pivot:
            left += 1
        if left <= right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
        else:
            break

    numbers[start], numbers[right] = numbers[right], numbers[start]
    return right


def quick_sort(numbers, start, end):
    if start >= end:
        return numbers

    p = partitioning(numbers, start, end)
    quick_sort(numbers, start, p - 1)
    quick_sort(numbers, p + 1, end)


def main():
    quick_sort(numbers, 0, len(numbers) - 1)
    print(numbers)


if __name__ == "__main__":
    main()
