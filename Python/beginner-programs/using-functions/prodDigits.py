def prodDigits(num):
    product = 1
    if num == 0:
        return 0
    while(num!=0):
        product *= (num%10)
        num = num//10
    return product
num = int(input("Enter the number: "))
print(prodDigits(num))
