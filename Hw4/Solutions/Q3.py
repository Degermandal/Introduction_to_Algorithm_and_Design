def findMaxCrossingSubarray(arr, low, mid, high):
    sum = 0
    LSum = float('-inf') #negative infinity for first assign
    for i in range(mid, low-1, -1):
        sum += arr[i]
        if (sum > LSum):
            LSum = sum
            LMax = i
    sum = 0
    RSum = float('-inf') #negative infinity for first assign
    for i in range(mid+1, high+1):
        sum += arr[i]
        if (sum > RSum):
            RSum = sum
            Rmax = i
    return LMax, Rmax, (LSum + RSum)

def findMaxSubarray(arr, low, high):
    if high == low: #baseCase one element situation
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        LLow, LHigh, LSum = findMaxSubarray(arr, low, mid)
        RLow, RHigh, RSum = findMaxSubarray(arr, mid+1, high)
        CLow, CHigh, CSum = findMaxCrossingSubarray(arr, low, mid, high) #crossLow ...

        if (LSum >= RSum and LSum >= CSum):
            return LLow, LHigh, LSum
        elif (RSum >= LSum and RSum >= CSum):
            return RLow, RHigh, RSum
        else:
            return CLow, CHigh, CSum

arr = [5, -6, 6, 7, -6, 7, -4, 3]
low, high, sum = findMaxSubarray(arr, 0, len(arr)-1)
print("Our list:", arr)
print("Maximum subarray:", arr[low: high+1])
print("The sum:", sum)