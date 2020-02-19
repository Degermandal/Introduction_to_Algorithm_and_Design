def findBest (arr1, arr2, low, high, lst):
    if low == high:
        return 1
    middle = (low + high) // 2
    findBest(arr1, arr2, low, middle, lst) #Left
    findBest(arr1, arr2, middle + 1, high, lst) #Right

    for i in range(len(arr1) -1):#I used difeerence between the two array
        lst.append(arr2[i+1] - arr1[i]) #gain amount
    return max(lst), (lst.index(max(lst))+1)

arr1 = [5, 11, 2, 21, 5, 7, 8, 12, 13, 0]
arr2 = [0, 7, 9, 5, 21, 7, 13, 10, 14, 20]
#arr2 = [0, 7, 9, 12, 21, 7, 13, 10, 14, 2]
#arr2 = [0, 5, 10, 2, 21, 5, 7, 8, 12, 13]
n = len(arr1)
lst = []
maxEl, index = findBest(arr1, arr2, 0, n-1, lst)

if(maxEl <= 0):
    print("No day to make money!!!")
else:
    print("Most Gain is", maxEl, "in ", index, "'th day.")
