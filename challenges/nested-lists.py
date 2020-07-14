# SRC: https://www.hackerrank.com/challenges/nested-list/problem
from itertools import filterfalse


if __name__ == '__main__':
    # Store results
    results = []

    # Variable lenght hackerrank input:
    for _ in range(int(input())):
        name = input()
        score = float(input())

        results.append((name, score))

    # Get the second lowest score
    score_target = sorted(set([i[1] for i in results]))[1]

    # Filter the students with that specific second lowest score:
    students = list(filterfalse(lambda x: x[1] != score_target, results))

    # Sort by the element in each tuple's 2nd position
    for name in sorted([i[0] for i in students]):
        print(name)
