from time import time
from merge import merge_sort
from bubble import bubble_sort
from heap import heap_sort
from counting import counting_sort
from quick import quick_sort


def time_statistics(numbers):
    fastest = []
    m_s_time = time()
    print(f'With "Merge sort method"')
    print(merge_sort(numbers))
    m_e_time = time()
    m_el_time = m_e_time - m_s_time
    fastest.append(m_el_time)
    print(f'It ran for {m_el_time} s.')

    h_s_time = time()
    print(f'With "Heap sort method"')
    print(heap_sort(numbers))
    h_e_time = time()
    h_el_time = h_e_time - h_s_time
    fastest.append(h_el_time)
    print(f'It ran for {h_el_time} s.')

    b_s_time = time()
    print(f'With "Bubble sort method"')
    print(bubble_sort(numbers))
    b_e_time = time()
    b_el_time = b_e_time - b_s_time
    fastest.append(b_el_time)
    print(f'It ran for {b_el_time} s.')

    c_s_time = time()
    print(f'With "Counting sort method"')
    print(counting_sort(numbers))
    c_e_time = time()
    c_el_time = c_e_time - c_s_time
    fastest.append(c_el_time)
    print(f'It ran for {c_el_time} s.')

    q_s_time = time()
    print(f'With "Quick sort method"')
    quick_sort(numbers)
    print(numbers)
    q_e_time = time()
    q_el_time = q_e_time - q_s_time
    fastest.append(q_el_time)
    print(f'It ran for {q_el_time} s.')

    fastest_method_time = min(fastest)
    slowest_method_time = max(fastest)
    fastest_m_i = fastest.index(fastest_method_time)
    slowest_m_i = fastest.index(slowest_method_time)
    if fastest_m_i == 0:
        fastest_method = 'Merge'
    elif fastest_m_i == 1:
        fastest_method = 'Heap'
    elif fastest_m_i == 2:
        fastest_method = 'Bubble'
    elif fastest_m_i == 3:
        fastest_method = 'Counting'
    else:
        fastest_method = 'Quick'
    if slowest_m_i == 0:
        slowest_method = 'Merge'
    elif slowest_m_i == 1:
        slowest_method = 'Heap'
    elif slowest_m_i == 2:
        slowest_method = 'Bubble'
    elif slowest_m_i == 3:
        slowest_method = 'Counting'
    else:
        slowest_method = 'Quick'

    print('\n')
    print(f'As You can see, the fastest sorting method is "{fastest_method} sort" with time {fastest_method_time},\n'
          f'and the slowest sorting method is "{slowest_method} sort" with time {slowest_method_time}.')
    print('\n')


numbers = [13, 24, 25, 26, 27, 15, 35, 36, 29, 49, 41, 37, 45, 68, 75, 25, 16]


def main():
    time_statistics(numbers)


if __name__ == "__main__":
    main()
