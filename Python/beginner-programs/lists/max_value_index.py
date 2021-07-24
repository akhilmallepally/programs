def maxValueInd(li):
    maxi = li[0]
    for i, num in enumerate(li):
        if num>maxi:
            maxi = num
            index = i
    return [index,maxi]

li = [1542,341,542,2673,1235]
print(maxValueInd(li))