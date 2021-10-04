def selection_sort(A):
    for i in range(len(A)-1):
        min_ele_index = i
        for j in range(i+1, len(A)):
            if A[j]< A[min_ele_index]:
                min_ele_index = j
        A[i], A[min_ele_index] = A[min_ele_index], A[i]
A = [6,3,2,5,2]
selection_sort(A)
print(A)
