#benim algorithmam sadece 2'li subsetler icindir.
def m(a, target):
    a.sort()
    right = len(a)-1
    left=0
    while(left<right):
        sum = a[left] + a[right]
        if(sum>target):
            right -= 1
        elif(sum<target):
            left += 1
        else:
            print("[", a[left], ",", a[right], "]")
            left += 1
            right -= 1

target = 0
print("The subsets:")
a = [-1, 6, 4, 2, 5, -7, -5]
m(a, target)