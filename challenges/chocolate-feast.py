import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m


def chocolateFeast(n, c, m):
    ate = wrappers = int(n / c)

    # while wrappers >= m:
    while wrappers and 0 <= wrappers % m < wrappers:

        ate += int(wrappers / m)
        wrappers = wrappers % m + int(wrappers / m)

    return ate


if __name__ == '__main__':
    # chocolateFeast(10, 2, 5)
    # chocolateFeast(12, 4, 4)
    chocolateFeast(6, 2, 2)