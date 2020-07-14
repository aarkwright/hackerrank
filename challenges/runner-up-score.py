if __name__ == '__main__':
    # Get hackerrank input
    n = int(input())
    scores = map(int, input().split())

    # Get unique scores (i.e.: exclude ties)
    # and get 2nd place
    print(list(sorted(set(scores)))[-2])