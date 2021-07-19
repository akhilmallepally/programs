listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

listThree = []
for i in listOne[1::2]:
    if i %2 !=0:
        listThree.append(listOne[i])
for j in range(len(listTwo)):
    if j % 2 == 0:
        listThree.append(listTwo[j])
print(listThree)