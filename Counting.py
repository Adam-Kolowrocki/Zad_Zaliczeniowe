numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]


def counting_sort(numbers):
    n_min = min(numbers)
    n_max = max(numbers)
    sorted_numbers = {}
    for i in range(n_min, n_max + 1):
        sorted_numbers[i] = 0
        for k in sorted_numbers:
            sorted_numbers[k] = numbers.count(k)
    sorted_list = []
    for key in range(n_min, n_max + 1):
        if sorted_numbers[key] > 0:
            sorted_list.append(key)
            sorted_numbers[key] -= 1
    return sorted_list


def main():
    counting_sort(numbers)
    print(counting_sort(numbers))


if __name__ == "__main__":
    main()
