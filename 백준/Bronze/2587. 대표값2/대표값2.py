li = []
for i in range(5):
    li.append(int(input()))
avg = sum(li)//len(li)
middle = sorted(li)[2]

print(avg)
print(middle)