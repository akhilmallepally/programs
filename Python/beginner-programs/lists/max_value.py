def maxValue(l1):
    maxi = l1[0]
    for num in l1:
        if num>maxi:
            maxi = num
    return maxi
l1 = [1,3,542,23,1235]
print(maxValue(l1))