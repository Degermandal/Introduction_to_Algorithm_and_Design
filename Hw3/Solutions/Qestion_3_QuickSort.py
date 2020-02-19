def partition(arr, low, high):#Complexity is Teta(n)
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if (low < high):
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr

arr = [21, 12, 11, 13, 5, 1]
n = len(arr)
t = quickSort(arr, 0, n-1)
print(t)