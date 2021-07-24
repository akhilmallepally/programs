def minValueInd(li):
    mini = li[0]
    for i, num in enumerate(li):
        if num<mini:
            mini = num
            index = i
    return [index, mini]

l = [8,3,5,3]
print(minValueInd(l))