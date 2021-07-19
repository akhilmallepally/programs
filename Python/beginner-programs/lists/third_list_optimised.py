listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

listThree = []

for i in listOne[1::2]:
    listThree.append(i)
for j in listTwo[0::2]:
    listThree.append(j)
print(listThree)