from time import time
def time_statistics(numbers):

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
        time_statistics(numbers)
    start_time = time()
    end_time = time()
