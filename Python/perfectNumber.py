#Program to check whether the given number is a perfect number or not


def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum+=i
    print("Sum of the dvisors is", sum)
    if sum == n:
        print("Sum of the divisors is equal to the input number. So, the given number is perfect")
    else:
        print("Sum of the divisors is not equal to the input number. So, the given number is not perfect")
perfect(int(input("Enter the number : ")))
