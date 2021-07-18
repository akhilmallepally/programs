n = 10
first, second = 0,1
count = 0
while(count<n):
    print(first)
    output = first+second
    first = second
    second = output
    count = count+1