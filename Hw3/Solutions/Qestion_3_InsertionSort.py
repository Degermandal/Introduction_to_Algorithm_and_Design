def insertionSort(arr, n):
    if n <= 1:
        return
    insertionSort(arr, n - 1)

    last = arr[n - 1]
    j = n - 2
    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last
    return arr

arr = [12, 11, 13, 5, 1, 21]
n = len(arr)
t = insertionSort(arr, n)
print(t)


