# SRC: https://www.hackerrank.com/challenges/np-polynomials/problem
import numpy as np


if __name__ == '__main__':
    # Get hackerrank input
    p = np.array([float(i) for i in input().split(' ')])
    x = int(input())

    print(np.polyval(p, x))