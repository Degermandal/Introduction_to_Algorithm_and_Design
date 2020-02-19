def findSpecial(arr):
    print("################") #print the elements of array
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j]," ", end='')
        print()
    print("################")

    for i in range(len(arr)-1):
        for j in range(len(arr[i])-1):
            # I used the first question equality
            e = (arr[i][j] + arr[i + 1][j + 1]) #A[i,j ] + A[i + 1,j + 1]
            d = (arr[i][j+1] + arr[i+1][j]) #A[i,j + 1] + A[i + 1,j ]
            if (e > d):
                print("You should change an element in the array")
                print("Replace the element:", arr[i][j + 1])
                arr[i][j+1] += (e-d) #I added because the element is not suitable for our array
                print("After replacement:",arr[i][j+1])
                findSpecial(arr)
            #else: e <= d It is okay for us

arr = [[37, 23, 22, 32],
       [21, 6, 7, 10],
       [53, 34, 30, 31],
       [32, 13, 9, 6],
       [43, 21, 15, 8]]

findSpecial(arr)