n, start, sum = 5, 2, 0
for i in range(0, n):
    sum += start
    start = (start*10)+2
print(sum)

