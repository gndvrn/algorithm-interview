# SELECTION SEARCH IMPLEMENTATION
# AUTHOR: https://github.com/gndvrn

import time
import random
from typing import *


def find_min_index(arr):
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index


def selection_sort(array: List[Union[int, float]],
                   reverse: bool = False) -> List[Union[int, float]]:
    sorted_arr = []

    arr = array.copy()

    for i in range(len(arr)):
        min_value = arr.pop(find_min_index(arr))
        if not reverse:
            sorted_arr.append(min_value)
        else:
            sorted_arr.insert(0, min_value)

    return sorted_arr


if __name__ == '__main__':
    massive = [random.randint(-5000, 5000) for _ in range(5000 + 1)]

    computation_times = []

    start_time = time.time()  # Track compilation time
    result = selection_sort(massive)  # Ascending selection sort
    end_time = time.time()

    computation_times.append(end_time - start_time)

    print('Average computational time: {} seconds'.format(
        sum(computation_times) / len(computation_times)), end='\n' * 2)

    assert result == sorted(massive)
