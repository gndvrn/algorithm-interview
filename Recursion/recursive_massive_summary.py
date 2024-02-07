# RECURSIVE ARRAY SUMMARY IMPLEMENTATION
# AUTHOR: https://github.com/gndvrn

from typing import *


def recursive_sum(arr: List[Union[int, float]]) -> Union[int, float]:
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])


if __name__ == '__main__':
    array = [2, 4, 6]

    print(recursive_sum(array))
