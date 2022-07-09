numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]


def mergesort(numbers):
    if len(numbers) == 1:
        return
    while len(numbers) > 1:
        l_idx = 0
        r_idx = len(numbers) - 1
        mid_idx = (l_idx + r_idx) // 2
        left = numbers[:mid_idx]
        right = numbers[mid_idx:]

        print(left)
        print(right)



def main():
    print('Given array is:', end="\n")
    print(numbers)
    print(type(numbers))
    print('Sorted array is:', end="\n")
    print(mergesort(numbers))
    print(type(mergesort(numbers)))


if __name__ == "__main__":
    main()
