
#assign each word of the following sentence to a variable and print the statement using the variables and print function 'All work and no play makes Jack a dull boy.'

a = ' All'
b = ' work'
c = ' and'
d = ' no'
e = ' play'
f = ' makes'
g = ' Jack'
h = ' a'
i = ' dull'
j = ' boy.' 

print(a+b+c+d+e+g+h+j)

#use paranthesis between operators
print(6*(1-2))

#bruce + 4 throws an error , name error as bruce is not defined
#asaigning bruce a value such that the result fot the above expr is 10
bruce = 6
print(bruce+4)

#Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be compounded for. Calculate and print the final amount after t years.

p = 10000
n = 12
r = 0.08
t_str = input("t, years")
t = int(t_str)   #or int(input('enter num'))


final_amount = p * ((1 + r / n) ** (n * t))

print(final_amount)


time = 2 
extra = 51
print(time+extra)



7. You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At
what time does the alarm go off? (Hint: you could count on your fingers, but this is not
what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)
8. Write a Python program to solve the general version of the above problem. Ask the user
for the time now (in hours), and ask for the number of hours to wait. Your program
should output what the time will be on the clock when the alarm goes off.