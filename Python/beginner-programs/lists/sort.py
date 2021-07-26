list1 = [2,4,5,3]
sorted_list = []
for i in range(len(list1)-1):
    if list1[i]<list1[i-1]:
        sorted_list.append(list1[i])
    else:
        list1[i]=list1[i+1]
    i=i+1
print(sorted_list)