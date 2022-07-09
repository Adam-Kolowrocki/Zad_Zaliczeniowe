numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]  # 17 elementów


def quick_sort(numbers):
    if len(numbers) == 0 or len(numbers) == 1:
        return numbers
    else:
        pivot = numbers[len(numbers) - 1]
        pivot_idx = len(numbers) - 1
        numbers_left = []
        numbers_right = []
        for i in range(0, len(numbers)):
            if numbers[i] > pivot:
                numbers_right.append(numbers[i])
                pivot_idx -= 1
            else:
                numbers_left.append(numbers[i])
                i += 1
        step_sort = numbers_left + numbers_right
        print(step_sort)




quick_sort(numbers)



# def main():
#     quick_sort(numbers, pivot, firtst, last)
#
# if __name__ == "__main__":
#     main()
