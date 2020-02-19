def getKey(item):
    return item[2]

def check(session, lst):
    if len(lst) == 0:
        return True
    if session[1] < lst[-1][2]:
        return False
    else:
        return True

def findOptimalList(lst):
    optimalLst = []
    lst = sorted(lst, key=getKey)
    for session in lst:
        if check(session, optimalLst):
            optimalLst.append(session)
    return optimalLst

lst = [['Session1', 9, 13], ['Session2', 10, 14],
        ['Session3', 13, 15], ['Session4', 11, 17],
        ['Session5', 15, 17], ['Session6', 12, 14],
        ['Session7', 14, 15], ['Session8', 10, 12]]
optimalLst = findOptimalList(lst)
print("The optimal session list is:")
for eachJob in optimalLst:
    print(eachJob)