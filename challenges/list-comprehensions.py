# SRC: https://www.hackerrank.com/challenges/list-comprehensions/problem

# TODO:
#  - Look into possible use of the combinations and/or permutatios modules from itertools
#  - https://docs.python.org/3/library/itertools.html#itertools.permutations

# Use standard library itertools to weed out sum condition
from itertools import filterfalse


if __name__ == '__main__':
    # Retrieve hackerrank type input
    x, y, z, n = [int(input()) for i in range(4)]

    # Make a list of combinations (this is ugly, but requested I guess)
    combis = [
        [a, b, c]
        for a in [_ for _ in range(x+1)]
        for b in [_ for _ in range(y+1)]
        for c in [_ for _ in range(z+1)]
    ]

    # Exclude combinations which have sum equal to 'n'
    out = list(filterfalse(lambda x: sum(x) == n, combis))
    print(out)
