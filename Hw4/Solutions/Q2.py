def kthElement(arr1, arr2, i):
    #the lengths for high values
    l1 = len(arr1)
    l2 = len(arr2)
    if (i > 0):
        return find(arr1, arr2, 0, 0, l1, l2, i-1)


def find(arr1, arr2, low1, low2, high1, high2, i):
    if (low1 == high1):
        return arr2[low2 + i]
    if (low2 == high2):
        return arr1[low1 + i]

    mid1 = (high1 - low1) // 2
    mid2 = (high2 - low2) // 2
    if (mid1 + mid2 < i):
        if (arr1[low1 + mid1] > arr2[low2 + mid2]):
            return find(arr1, arr2, low1, low2+mid2+1, high1, high2, i-mid2-1)
        else:
            return find(arr1, arr2, low1+mid1+1, low2, high1, high2, i-mid1-1)
    else:
        if (arr1[low1 + mid1] > arr2[low2 + mid2]):
            return find(arr1, arr2, low1, low2, low1+mid1, high2, i)
        else:
            return find(arr1, arr2, low1, low2, high1, low2+mid2, i)


arr1 = [1, 4, 21]
arr2 = [7, 8, 9, 32, 43]

t1 = kthElement(arr1, arr2, 1)
t2 = kthElement(arr1, arr2, 2)
t3 = kthElement(arr1, arr2, 3)
t4 = kthElement(arr1, arr2, 4)
t5 = kthElement(arr1, arr2, 5)
t6 = kthElement(arr1, arr2, 6)
t7 = kthElement(arr1, arr2, 7)
t8 = kthElement(arr1, arr2, 8)
print("List->", t1, t2, t3, t4, t5, t6, t7, t8)

arr1 = [2, 7, 9, 11]
arr2 = [3, 8, 20, 32, 43]

test1 = kthElement(arr1, arr2, 2)
test2 = kthElement(arr1, arr2, 7)

print("Test1: second element is", test1)
print("Test2: seventh element is", test2)

