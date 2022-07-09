numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]  # 17 elementów


def quick_sort(numbers):
    if len(numbers) == 0 or len(numbers) == 1:
        return numbers
    else:
        print(f'na początku lista wygląda tak {numbers}')
        p = 0
        r = len(numbers)
        q = len(numbers) - 1
        pivot = numbers[len(numbers) - 1]
        i = 0
        while i <= q:
            print(f'wartość i = {i}')
            if numbers[i] > pivot:
                print(f'wartość numbers[i] = {numbers[i]} więc przenoszę za pivot')
                numbers.insert(q + 1, numbers.pop(i))
                q -= 1
            else:
                print(f'wartość numbers[i] = {numbers[i]} więc przechodzę dalej')
                i += 1
                pass
        print(f'po pętli for lista wygląda tak {numbers}')
        print(len(numbers))




quick_sort(numbers)



# def main():
#     quick_sort(numbers, pivot, firtst, last)
#
# if __name__ == "__main__":
#     main()
