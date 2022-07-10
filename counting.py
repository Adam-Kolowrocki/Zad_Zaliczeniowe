def counting_sort(numbers):
    n_min = min(numbers)
    n_max = max(numbers)
    sorted_dic = {}
    for i in range(n_min, n_max + 1):
        sorted_dic[i] = 0
        for k in sorted_dic:
            sorted_dic[k] = numbers.count(k)
    sorted_numbers = []
    for key in range(n_min, n_max + 1):
        while sorted_dic[key] > 0:
            if sorted_dic[key] > 0:
                sorted_numbers.append(key)
                sorted_dic[key] -= 1
    sorted_numbers.reverse()
    return sorted_numbers


numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]


def main():
    print(numbers)
    print(counting_sort(numbers))


if __name__ == "__main__":
    main()
