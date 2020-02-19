def insertionSortRecursive(arr, n, t):
    if n < 2: #Base Case
        return 1
    insertionSortRecursive(arr, n - 2, t)
    if n-1 < t: #Half part condition
        #even or odd was important for my algorithm so I seperated
        if(t%2 == 0): #even
            arr[n-1], arr[n-1 + t-1] = arr[n-1 + t-1], arr[n-1]
        if(t%2 == 1):#odd
            arr[n-1], arr[n-1 + t] = arr[n-1 + t], arr[n-1]

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end="  ")

#arr = ["Black", "Black", "Black", "White", "White", "White"]
arr = ["Black", "Black", "Black", "Black", "White", "White", "White", "White"]
#arr = ["Black", "White"]
n = len(arr)
t = int(n/2)
insertionSortRecursive(arr, n, t)
printArray(arr, n)

