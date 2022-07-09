# Napisz funkcję przeszukiwania połówkowego (binarenego),
# która przyjmuje dwa parametry - szukany element oraz listę elementów.
# Zwraca informację czy element jest obecny na liście, albo nie.

data = [2, 3, 3, 6, 7, 12, 12, 15, 18, 21, 25, 34, 36, 44, 45, 46, 48, 49, 56, 56, 58, 59, 69, 78, 85]
elem = int(input(f'Podaj wartość do odnalezienia na liście elementów -> '))


def search(data, elem):
    lb = 0
    ub = len(data) - 1
    while lb <= ub:
        mid_v = (lb + ub) // 2
        if data[mid_v] == elem:
            return mid_v
        else:
            if data[mid_v] < elem:
                lb = mid_v + 1
            else:
                ub = mid_v - 1
    return False


def main():
    print(f'Program do wyszukiwania połówkowego.')
    if search(data, elem):
        print(f'Element {elem} znajduje się na liście na pozycji {search(data,elem) + 1}.')
    else:
        print(f'{elem} nie ma na liście.')


if __name__ == "__main__":
    main()
