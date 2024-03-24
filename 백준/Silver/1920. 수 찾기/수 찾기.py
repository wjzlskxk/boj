n = int(input())
arr_n = set(map(int,input().split()))
m = int(input())
arr_m = list(map(int,input().split()))

for num in arr_m:
    print(1) if num in arr_n else print(0)