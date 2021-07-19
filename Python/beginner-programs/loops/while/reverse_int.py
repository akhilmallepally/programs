num = 12345
print(f'num before loop : {num}')
reverse_number = 0
while num>0:
    reminder = num %10
    reverse_number = reverse_number*10 + reminder
    num = num//10
print(f'reminder after all iterations : {reminder}')
print(f'num after all iterations : {num}')
print(f'Reserved num : {reverse_number}')