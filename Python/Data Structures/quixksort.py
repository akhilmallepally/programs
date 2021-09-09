#Enter Python code here and hit the Run button.
A = [5,1,3,2]
swapped = True
while swapped:
    
    for i in range(len(A)-1):
        if A[i]>A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            #swapped = True
        else:
            swapped = False
    
print(A)
