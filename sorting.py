import random
clear = '\n'*25


def data_input(source_choice):
    source_choice = menu()
    if source_choice == 'f':
        with open('naturals_list.txt') as f:
            data_list = f.readline()
            return data_list
    elif source_choice == 'r':
        data_list = []
        for i in range(0, 9):
            data_list.append(random.randint(10, 99))
            return data_list
    elif source_choice == 'k':
        data_list = []
        print(f'Type 10 natural numbers.')
        while len(data_list) < 10:
            user_input = int(input(f'Type a number ->'))
            if user_input > 0 and user_input // user_input == 0:
                data_list.append(user_input)
            else:
                print(f'Wrong number... Type natural numbers.')
        return data_list


def menu():
    # print(clear)
    print(f'You can choose the source of natural numbers to sort.')
    print(f' Type \n "F" for file, \n "K" for keyboard or \n "R" for random generated numbers.\n')
    source_choice = input(f'What is Your Choice ->')
    # print(clear)
    print(f'Now, You can choose sorting metod.')
    print(f' Type \n"M" for Merge Sort, \n "H" for Heap Sort, \n "B" for BubbleSort, \n '
          f'"C" for Counting Sort or \n "Q" for Quick Sort.')
    sort_choice = input(f'What is Your Choice ->')
    return source_choice.lower(), sort_choice.lower()


def main():
    # print(clear)
    print(f'******** Sorting ********'.center(20))
    # input(f'Press Enter to begin...'.center(30))
    menu()


if __name__ == "__main__":
    main()
