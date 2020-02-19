import math
#I though like find largest tehn can find the median
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def kthLargestElement(arr, k):
    low = 0
    high = len(arr) - 1
    pi = partition(arr, low, high)
    if pi == (high - k + 1):
        return arr[pi]
    elif pi > (high - k + 1):
        return kthLargestElement(arr[:pi], k - (high - pi + 1))
    else:
        return kthLargestElement(arr[pi + 1:high + 1], k)

arr = [1, 3, 2, 5, 6, 4, 10, 9, 8, 11, 7]
length = len(arr)
#even and odd situations
if ( length % 2 == 1): # just calculate
    element = int((length/2)) + 1
    result = kthLargestElement(arr, element)
if (length % 2 == 0): # calculate summation and divide to 2
    first = kthLargestElement(arr, int((length/2)) +1)
    second = kthLargestElement(arr, int((length/2)))
    result = math.ceil((first+second)/2) #ceil function for correct decision

print("The median:", result)
