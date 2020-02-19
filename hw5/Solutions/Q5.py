def greedySum(arr, opCount):
    gSum = 0
    largeD, min = -1, arr[0]
    for i in range(0, len(arr)):
        gSum += arr[i]
        if (arr[i] % opCount == 0 and largeD < arr[i]):
            largeD = arr[i]
        if arr[i] < min:
            min = arr[i]

    if largeD == -1:
        return gSum

    result = (gSum - min - largeD + (opCount * min) + (largeD // opCount))
    return min(gSum, result)

arr = [7, 5, 13, 17]
opCount = 2
print("Min number of operations:", greedySum(arr, opCount))
