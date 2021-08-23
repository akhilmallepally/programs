#Enter Python code here and hit the Run button.
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i>0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1]= key
A = [1,3,2,5,6,4,9,7]
insertion_sort(A)

lst= []
for value in A:
    lst.append(value)
print(lst)
