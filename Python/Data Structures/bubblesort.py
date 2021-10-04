def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                
A = [3,5,1,6,2]
bubble_sort(A)
print(A)
