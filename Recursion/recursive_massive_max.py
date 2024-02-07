# RECURSIVE FINDING OF THE MAX ELEMENT IN THE ARRAY
# AUTHOR: https://github.com/gndvrn

from typing import *


def recursive_max(arr: List[Union[int, float]]) -> Union[int, float]:
    if len(arr) == 1:
        return arr[0]
    else:
        m = recursive_max(arr[1:])
        if m > arr[0]:
            return m
        else:
            return arr[0]


if __name__ == '__main__':
    array = [2, 86, 6, 19, 98, 21]

    print(recursive_max(array))