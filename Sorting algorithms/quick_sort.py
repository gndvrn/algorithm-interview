# QUICK SORT ALGORITHM IMPLEMENTATION
# AUTHOR: https://github.com/gndvrn

from typing import *
import time


def qsort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    if len(arr) < 2:  # If the basic situation was reached
        return arr
    else:
        # Picking mid element as a pivot
        pivot_i = (len(arr) - 1) // 2
        pivot = arr[pivot_i]

        # Array of elements that are smaller than pivot
        left_arr = [i for i in arr[:pivot_i] + arr[pivot_i + 1:] if i <= pivot]

        # Array of elements that are greater than pivot
        right_arr = [i for i in arr[:pivot_i] + arr[pivot_i + 1:] if i > pivot]

        return qsort(left_arr) + [pivot] + qsort(right_arr)  # Recursively sorting array...


if __name__ == '__main__':
    array = [16, 34, 2, 86, 6, 19, 98, 21]

    start_time = time.time()
    quick_sorted_array = qsort(array)
    end_time = time.time()

    print('Computational time: {}'
          .format(round(end_time - start_time, 5)), end='\n' * 2)

    print(quick_sorted_array)

    try:
        assert quick_sorted_array == sorted(array)
    except AssertionError:
        raise Exception('Sorting was done incorrectly :(')
