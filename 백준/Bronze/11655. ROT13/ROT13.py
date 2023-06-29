w = input()
w_list = [i for i in w]
for i in range(len(w_list)):
    if w_list[i].isupper():
        w_list[i] = chr((ord(w_list[i])-65+13)%26+65)
    elif w_list[i].islower():
        w_list[i] = chr((ord(w_list[i])-97+13)%26+97)
print(*w_list,sep='')