'''

cellphone attributes : size , weight, dimensions, 
cellphone methods : scroll ,  
'''
'''
Write a program that uses a for loop to print
One of the months of the year is January
One of the months of the year is February
'''

months =['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'aug', 'sept', 'oct', 'nov', 'dec']
for month in months:
  print('One of the months of the year is ', month)
  

for i in range(1000):
  print('print this 1000 times')
  
  '''
Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
(a) Write a loop that prints each of the numbers on a new line.
(b) Write a loop that prints each number and its square on a new line.
(c) Write a loop that adds all the numbers from the list into a variable called total. You
should set the total variable to have the value 0 before you start adding them up,
and print the value in total after the loop has completed.
(d) Print the product of all the numbers in the list. (product means all multiplied to-
gether)'''

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
  print(i)

for i in xs:
  print(i, i*i)

total = 0
for i in xs:
  total += i
print(total)

product = 1 
for i in xs:
  product *= 1 
print(product)
