# SRC: https://www.hackerrank.com/challenges/np-polynomials/problem
import numpy as np


if __name__ == '__main__':
    # Get hackerrank input
    N = int(input())
    A = [[float(i) for i in input().split(' ')] for _ in range(N)]

    determinant = np.linalg.det(A)

    print(round(determinant, ndigits=2))