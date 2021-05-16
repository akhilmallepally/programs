#Sum of Divisors

def sumPdivisors(n):
    sum =0
    for i in range(1,n):
        if n%i ==0:
            sum = sum + i
    print(sum)
sumPdivisors(int(input("enter the number : ")))
