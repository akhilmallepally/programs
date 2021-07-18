first = 0
second = 1
print(first)
print(second)
for i in range(1, 10):
    output = first+second
    print(output, end = " ")
    first = second
    second = output
    