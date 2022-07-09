numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]


def merge_sort(numbers):
    if len(numbers) > 1:
        left_numbers = numbers[:len(numbers) // 2]
        right_numbers = numbers[len(numbers) // 2:]

        merge_sort(left_numbers)
        merge_sort(right_numbers)

        i = 0
        j = 0
        k = 0
        while i < len(left_numbers) and j < len(right_numbers):
            if left_numbers[i] < right_numbers[j]:
                numbers[k] = left_numbers[i]
                i += 1
            else:
                numbers[k] = right_numbers[j]
                j += 1
            k += 1
        while i < len(left_numbers):
            numbers[k] = left_numbers[i]
            i += 1
        while j < len(right_numbers):
            numbers[k] = right_numbers[j]
            j += 1
    return numbers


def main():
    print('Given array is:', end="\n")
    print(numbers)
    print(type(numbers))
    print('Sorted array is:', end="\n")
    print(merge_sort(numbers))
    print(type(merge_sort(numbers)))


if __name__ == "__main__":
    main()
