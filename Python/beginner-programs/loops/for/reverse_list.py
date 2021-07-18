list1 = [10, 20, 30, 40, 50]
list2 = []
start = len(list1)-1
stop = -1
step = -1
for i in range(start, stop, step):
    list2.append(list1[i])
print(list2)