list = [2, 1, 5, 3, 4]
c = 0
dic = {}
for i in list:
    c += 1
    dic[c] = i
list_2 = []
for x in range(1, len(list) + 1):
    for key, value in dic.items():
        if x == value:
            list_2.append(key)
print(list_2)