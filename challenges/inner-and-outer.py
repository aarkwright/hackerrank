# SRC: https://www.hackerrank.com/challenges/np-inner-and-outer/problem
import numpy as np


if __name__ == '__main__':
    # Get hackerrank input
    a = np.array([int(i) for i in input().split(' ')])
    b = np.array([int(i) for i in input().split(' ')])

    # Inner product:
    # https://en.wikipedia.org/wiki/Inner_product_space
    print(np.inner(a, b))

    # Outer product:
    # https://en.wikipedia.org/wiki/Outer_product
    print(np.outer(a, b))