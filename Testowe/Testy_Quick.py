numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]  # 17 elementów


def quick_sort(numbers):
    if len(numbers) == 0 or len(numbers) == 1:
        return numbers
    else:
        pivot = numbers[len(numbers) - 1]
        pivot_idx = len(numbers) - 1
        i = 0
        while i <= pivot_idx:
            przejście = 0
            print(f'index i = {i}')
            print(f'pivot = {pivot}')
            print(f'pivot index = {pivot_idx}')
            print(f'przed sortowaniem {numbers}')
            print(f'sprawdzany element {numbers[i]}')
            if numbers[i] > pivot:
                numbers.insert(pivot_idx + 1, numbers.pop(i))
                pivot_idx -= 1
                print(f'lista po dodaniu elementu po pivocie {numbers}')
            else:
                i += 1
                print(f'lista po dodaniu elementu przed pivotem {numbers}')
            przejście += 1
            print(f'po prześciu {przejście} lista wygląda tak {numbers}')
            # return numbers
        # quick_sort(numbers)
    print(f'po sortowaniu {numbers}')


quick_sort(numbers)



# def main():
#     quick_sort(numbers, pivot, firtst, last)
#
# if __name__ == "__main__":
#     main()
