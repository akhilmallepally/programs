
list1 = [] #empty list
list2 = [1 , 2, 5]  #list of imtegerz
list3 = [1, 'hi', 1.43] #mixed list
list4 = [4, [2,'yes'], 3.2, 9, 'akhil'] #nested list

#indexing
list5 = [2, 'hello', 1.34, 'nano', 554]
print(list5[2])
print(list5[1])

#negative indexing
print(list5[-1])
print(list5[-3])

#slicing or accessing a range of items
print(list5[:]) #all elements
print(list5[2:5]) #from 3rd item to 5th 
print(list5[:3]) #from beginning to 3rd item
print(list5[1:]) #from 2nd item to end

#changing items of a list
list6 = [1, 2, 3, 4]
list6[2] = 'hi'
print(list6)
list7 = [1,6,2,5]
list7[2:4] = [7,8,0] #changing a ranfe of items
print(list7)

#append and extend
list6.append(4) #adding an element
print(list6)
list6.extend(list7) #or list6.append([1,6,3])#adding a new list or items of a list
print(list6)

#using + and * operators
list8 = [1,5,7]
print(list8 + [6,9]) #concatenation / adding two lists
list9 = [0,2,4]
print(list8 + list9)

print(list8 * 2) #repeating list8 2times
print('ab' * 4 ) #repeating ab 4 times
print(['hi', 'hello'] * 3) #repeating given lost 3 times

#using insert
list8.insert(1,9) #inserting 9 at 1st index
print(list8)

list9[2:2] = [7,8,9] #inserting the list items from 2nd index. if we dont mention :2 , it eleminates the last items
print(list9)

#delete 
list10 = [1,5,2,8,6,0,22]
del list10[5] #deletes 3rd index /4th item
print(list10)

del list10[1:3] #deletes a range of items
print(list10) 

del list10 # deletes entire list
#print(list10) #results in an error : no list defined

#using remove, pop, clear
list11 = [2,1,71,91,30,2]
list11.remove(2) #removes the item '2'(if multiple 2's are there, all are removed), not the index
print(list11)

list11.pop(1) #pops index1
print(list11)

list11.pop() #pops last item
print(list11)

list11.clear()
print(list11) #empties the list, doesn't delete

#copying the list
list12 = [1,28,56,27,91]
list13 = list12 
print(list13)

list12.append(5)
print(list12)
print(list13) #changing in list12 also cjanges in list13 as they are pointing to the same list13

list13 = list12.copy() #using copy
list12[3] = 120
print(list12)
print(list13)

#loop through a list
names = ['jane', 'john', 'killbill']
for name in names:
  print('name is', name)
  
#check whether an item is in a list or not
print('jane' in names) #true
print('akhil' in names) #false

#indexing a nested list
list14 = [1,92,74,6,[4,3,7]] #nested list
print(list14[4])
print(list14[4][1])

