def tower(n, source, destination, auxiliary):
    if n==1: #base case
        print("move disk from source "+source+" to destination"+destination)
        return 
    tower(n-1, source, destination, auxiliary)
    print("move disk "+str(n)+" from source "+source+" to destination"+destination)
    tower(n-1, auxiliary, destination, source)
  
n = 5
tower(n, "A","B","C")
