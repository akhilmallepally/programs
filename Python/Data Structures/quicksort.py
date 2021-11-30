def quicksort(arr, low, high):
    if len(arr)==1:
        return arr
    else:    
        if low<high:
            p = partition(arr, low, high)
            quicksort(arr, low, p-1)
            quicksort(arr, p+1,high)
    return arr

def partition(arr, low, high):
    print("given array is ", arr)
    pivot = arr[high]
    i = low-1
    print("low index is ", low)
    print("i index is ", i)
    print("pivot value is arr[high] = ", pivot)
    print("loop bgins ******************************* ")
    while low<high:
        print("arr[low] is", arr[low])
        print("pivot is ", pivot)
        if arr[low]<=pivot:
            print("if", arr[low], "<=", pivot, "increase i value and swap", arr[i], "and", arr[low])
            i=i+1
            arr[i], arr[low]= arr[low], arr[i]
        else:
            print(arr[low],"is >", pivot, "so no swapping took place")
        low = low + 1
        print("increment low by 1 and the new low is ", low)
        print(arr)
    print("loop exited ************************")
    arr[i+1], arr[high]= arr[high], arr[i+1]
    print("values swapped high and i+1")
    print(arr)
    return i+1
    
a = [2,3,51,6,1,0]
low = 0
high = len(a)-1
print(quicksort(a,low,high))
