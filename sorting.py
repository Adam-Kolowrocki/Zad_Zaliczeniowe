from random import randint
from merge import merge_sort
from bubble import bubble_sort
from heap import heap_sort
from counting import counting_sort
from quick import quick_sort
from time_stat import time_statistics
clear = '\n'*25


def sort_metod(sort_choice, numbers):
    if sort_choice == 'm':
        return merge_sort(numbers)
    elif sort_choice == 'h':
        return heap_sort(numbers)
    elif sort_choice == 'b':
        return bubble_sort(numbers)
    elif sort_choice == 'c':
        return counting_sort(numbers)
    elif sort_choice == 'q':
        quick_sort(numbers)
        return numbers
    elif sort_choice == 't':
        return time_statistics(numbers)


def data_input(source_choice):
    if source_choice == 'f':
        with open('n_numbers.txt') as f:
            numbers = f.readline()
            numbers = numbers.rsplit(", ")
            for i in range(0, len(numbers)):
                numbers[i] = int(numbers[i])
            return numbers
    elif source_choice == 'r':
        numbers = []
        for i in range(0, 30):
            n = randint(10, 99)
            numbers.append(n)
        return numbers
    elif source_choice == 'k':
        while True:
            numbers = []
            num_count = int(input(f'How many natural numbers do You want to sort ?'))
            if num_count <= 0:
                print(f'Wrong number... Type natural number.')
                continue
            for i in range(1, num_count + 1):
                user_input = int(input(f'Type {i} number ->'))
                if user_input > 0:
                    numbers.append(user_input)
                else:
                    print(f'Wrong number... Type natural numbers.')
            return numbers


def menu():
    print(f'You can choose sorting metod.')
    print(f'Type \n "M" for Merge Sort, \n "H" for Heap Sort, \n "B" for BubbleSort, \n '
          f'"C" for Counting Sort or \n "Q" for Quick Sort.')
    print('\n')
    print(f'Or Yoy can test the speed of all five methods on the same list of numbers. ')
    print(f'Fot this, type "T".')
    print('\n')
    sort_choice = input(f'What is Your Choice ->')
    print(clear)
    print(f'And the source of natural numbers to sort.'.center(140))
    print(f' Type \n "F" for file, \n "K" for keyboard or \n "R" for random generated numbers.\n')
    source_choice = input(f'What is Your Choice ->')
    print(clear)
    return source_choice.lower(), sort_choice.lower()


def main():
    print(clear)
    print('\n')
    print(f'******** Sorting ********'.center(140))
    print('\n')
    print(f'This is a project made for sorting natural numbers.'.center(140))
    print('\n')
    input(f'Press Enter to begin...'.center(140))
    source_choice, sort_choice = menu()
    numbers = data_input(source_choice)
    print(clear)
    print(f'Numbers You wanted to sort was :')
    print(numbers)
    print('\n')
    print(f'After sorting the list looks like this:')
    print(sort_metod(sort_choice, numbers))


if __name__ == "__main__":
    main()
