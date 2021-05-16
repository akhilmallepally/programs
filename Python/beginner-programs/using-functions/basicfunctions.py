def func(x) :
    print(x)

func(10)
func(20)

#a function prints whenever it is called. here, it prints both 10 & 20 as output because the function is called twice.

def stuff():
    print('Hello')
    return
    print('World')

stuff()

#understanding the return statement is crucial in functions. Here, when the stuff() function is called, only Hello is printed because after the return statement the next line of command is not executed(it exits there in the function).