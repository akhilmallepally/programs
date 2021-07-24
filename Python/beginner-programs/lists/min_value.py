def min_value(li):
    mini = li[0]
    for num in li:
        if num < mini:
            mini = num
    return mini

li = [6,3,4,2]
print(min_value(li))