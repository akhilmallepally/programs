#Print a mersenne prime from user input

n = int(input("enter a number"))
a = (2**n)-1
if n>1:
    for i in range(2,n):
        if n%i == 0:
            print("not prime")
        elif a%i == 0:
            print(" not mersenne prime")
            
        else:
            print("mersenne prime")
            print(a)
        break
else:
    print("not valid")