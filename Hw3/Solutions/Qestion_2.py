import math

def weighCoins(arr, low, high): #I found the total of weighs of coins
    sum = 0
    i = low
    for i in range(high):
        sum += arr[i]
    return sum

def findFakeCoin(arr, low, high): #I seperated to 3 situation
    if high == low: #if equal
        print("fake coin index: ", high)
        return high

    elif low == (high-1): #if k-1
        if arr[high] > arr[low]:
            print("fake coin index: ", high)
            return high
        else:
            print("fake coin index: ", low)
            return low

    elif low == (high - 2): #if k-2
        if arr[high] > arr[high-1]:
            print("fake coin index: ", high)
            return high
        elif arr[high-1] > arr[low]:
            print("fake coin index: ", high-1)
            return (high-1)
        else:
            print("fake coin index: ", low)
            return low
    else:
        thirdsOfDifference = math.ceil(((high+1) - low)/3) #n/3
        lowMid = thirdsOfDifference + low
        highMid = (thirdsOfDifference*2) + low

        sumLow = weighCoins(arr, low, lowMid)
        sumMid = weighCoins(arr, lowMid, highMid)
        #print("thoD->", thirdsOfDifference, " loM->", lowMid, " hM->", highMid, " sL->", sumLow, " sM->", sumMid)
        if sumLow == sumMid:
            findFakeCoin(arr, highMid, high)
        elif sumLow > sumMid:
            findFakeCoin(arr, low, lowMid-1)
        else:
            findFakeCoin(arr, lowMid, highMid-1)

arr = [1, 1, 1, 2, 1, 1, 1, 1]
#arr = [1, 1, 1, 1, 2, 1, 1, 1]
#arr = [1, 1, 1, 1, 1, 2, 1, 1]
ln  = len(arr)
findFakeCoin(arr, 0, ln)


