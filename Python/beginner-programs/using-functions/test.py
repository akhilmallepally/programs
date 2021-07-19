def outerFun(a, b):
    def innerFun(c, d):
        pass
    return innerFun(a, b)
    return a

result = outerFun(5, 10)
print(result)