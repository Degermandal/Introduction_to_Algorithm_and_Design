def findBest(arr):
    middle1 = []
    middle2 = []
    for i in range(len(arr)):
        if i % 2 == 0:
            middle1.append(arr[i])
        if i % 2 == 1:
            middle2.append(arr[i])
#we should odd number rows for finding leftmost min element
    #t1 = findBestHelper(middle1)
    t2 = findBestHelper(middle2)
    return t2

def findBestHelper (arr):
    if len(arr) == 0:
        return 1

    for i in range(len(arr)):
        for j in range(len(arr[i]) // 2): #I used the problem equalities
            a = i+1
            b = j+1
            e = arr[j][a] + arr[i][b]
            d = arr[i][a] + arr[j][b]
            while(e > d):
                if(arr[j][a] >= arr[i][a]):
                    return arr[i][a]
                if(arr[i][b] >= arr[j][b]):
                    return arr[j][b]

arr =     [[37, 23, 24, 32],
          [21, 6, 7, 10],
          [53, 34, 30, 31],
          [32, 13, 9, 6],
          [43, 21, 15, 8]]

t1 = findBest(arr)  # Left
print("Leftmost minimum element:", t1)

print(".............................")

arr =     [[10, 17, 13, 28, 23],
          [17, 22, 16, 29, 23],
          [24, 28, 22, 34, 24],
          [11, 13, 6, 17, 7],
          [45, 44, 32, 37, 23],
          [36, 33, 19, 21, 6],
          [75, 66, 51, 53, 34]]

t1 = findBest(arr)  # Left
print("Leftmost minimum element:", t1)
