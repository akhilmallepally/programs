list1 = [54, 44, 27, 79, 91, 41]
temp = list1.pop(4) # removes element at index 4 and stores the element in temp variable
print(f' Removed element : {temp}')
list1.insert(2, temp)
list1.append(temp)
print(f'list after appending the removed element at 2nd and last index : {list1}')