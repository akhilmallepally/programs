num = 76542
reverse_number = 0
for i in range(len(str(num))):
    reminder = num%10
    reverse_number = (reverse_number *10)+reminder
    num = num//10
print(reverse_number)