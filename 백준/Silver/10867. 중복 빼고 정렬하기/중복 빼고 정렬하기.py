n = int(input())

li = list(map(int,input().split()))

sorted(set(li))

print(*sorted(set(li)))