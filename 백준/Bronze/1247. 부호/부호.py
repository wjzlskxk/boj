from sys import stdin

for _ in range(3):
    n = int(stdin.readline())
    li = [int(stdin.readline())for i in range(n)]
    if sum(li) == 0:
        print(0)
    elif sum(li) > 0:
        print('+')
    else:
        print('-')