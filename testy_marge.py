numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]
l_idx = 0
r_idx = len(numbers) - 1


def mergesort(numbers):
    if len(numbers) == 1:
        return
    if len(numbers) > 1:
        mid_idx = len(numbers) // 2
        left = numbers[:mid_idx]
        right = numbers[mid_idx:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1
    return numbers


def main():
    print('Given array is:', end="\n")
    print(numbers)
    print(type(numbers))
    print('Sorted array is:', end="\n")
    print(mergesort(numbers))
    print(type(mergesort(numbers)))


if __name__ == "__main__":
    main()
