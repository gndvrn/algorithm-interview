# RECURSIVE ARRAY LENGTH IMPLEMENTATION
# AUTHOR: https://github.com/gndvrn

from typing import *


def recursive_len(arr: List[Union[int, float]]) -> Union[int, float]:
    if len(arr) == 1:
        return 1
    else:
        return 1 + recursive_len(arr[1:])


if __name__ == '__main__':
    array = [2, 4, 6, 18, 35]

    print(recursive_len(array))