import numpy as np
assign = {'match': 2, 'mismatch': -2, 'gap': -1}

def find(a, b):
    if a == b:
        return assign['match']
    elif a == '-' or b == '-':
        return assign['gap']
    else:
        return assign['mismatch']

def findMinCost(s1, s2):
    m, n = len(s1), len(s2)
    score = np.zeros((m + 1, n + 1))
    for i in range(m + 1):
        score[i][0] = assign['gap'] * i
    for j in range(n + 1):
        score[0][j] = assign['gap'] * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = score[i - 1][j - 1] + find(s1[i - 1], s2[j - 1])
            delete = score[i - 1][j] + assign['gap']
            insert = score[i][j - 1] + assign['gap']
            score[i][j] = max(diag, delete, insert)
    result1, result2 = "",""
    i, j = m, n

    while i > 0 and j > 0:
        ss = score[i][j]
        sD = score[i - 1][j - 1]
        sL = score[i][j - 1]
        sU = score[i - 1][j]

        if ss == sD + find(s1[i - 1], s2[j - 1]):
            a1, a2 = s1[i - 1], s2[j - 1]
            i, j = i - 1, j - 1
        elif ss == sU + assign['gap']:
            a1, a2 = s1[i - 1], '-'
            i -= 1
        elif ss == sL + assign['gap']:
            a1, a2 = '-', s2[j - 1]
            j -= 1
        print("a1 =", a1, "# a2 =", a2)
        result1 += a1
        result2 += a2

    result1 = result1[::-1]
    result2 = result2[::-1]
    lR1 = len(result1)
    cost = 0
    for i in range(lR1):
        a1 = result1[i]
        a2 = result2[i]
        if a1 == a2:
            cost += find(a1, a2)
        else:
            cost += find(a1, a2)

    print("Min cost is", cost)

findMinCost("ALIGNMENT", "SLIME")
