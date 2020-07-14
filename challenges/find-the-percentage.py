# SRC: https://www.hackerrank.com/challenges/finding-the-percentage/problem
from statistics import mean

if __name__ == '__main__':
    # hackerrank style inputs :)
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # main
    score = student_marks[query_name]
    print(f'{mean(score):.2f}')