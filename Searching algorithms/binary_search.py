# BINARY SEARCH IMPLEMENTATION
# AUTHOR: https://github.com/gndvrn

import time
from typing import *


def binary_search(sorted_arr: List[Union[int, float]],
                  item: Union[int, float]) -> Union[int, None]:
    low_index = 0
    high_index = len(sorted_arr) - 1

    while low_index <= high_index:  # Until there is one element left

        mid_index = (low_index + high_index) // 2  # Choosing middle element

        if sorted_arr[mid_index] == item:
            return mid_index
        elif sorted_arr[mid_index] < item:
            low_index = mid_index + 1  # +1 because we already know that mid_index item is smaller
        else:
            high_index = mid_index - 1  # +1 because we already know that mid_index item is greater

    return None  # Returning None if there is no such element in the array


if __name__ == '__main__':
    sorted_array = [i for i in range(-2500, 2500 + 1)]
    items = [1681, -1065, 0, 8912]

    computation_times = []

    results = {}

    for i in items:
        start_time = time.time()  # Track compilation time
        search_result = binary_search(sorted_array, i)
        end_time = time.time()

        computation_times.append(end_time - start_time)
        results[i] = search_result

    print('Average computational time: {}'.format(
        sum(computation_times) / len(computation_times)), end='\n' * 2)

    print(results)
