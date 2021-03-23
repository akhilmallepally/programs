#Program to check whether the given numbers are amicable 

def perfect(m,n):
    sum = 0 
    for i in range(1,n):
        if n%i == 0:
            sum+=i
      
    if sum == m:
        print(m,n)
    else:
        print("not amicable")
perfect(int(input("enter m : ")),int(input("enter n :")))
