def findCost(cities, months, operatingCost, relocationCost):
    dpTable = [[0 for x in range(months)] for y in range(cities)]
    path = [[0 for x in range(months)] for y in range(cities)]
    for c in range(cities):
        dpTable[c][0] = operatingCost[c][0]
        path[c][0] = c

    month = 1
    while month < months:
        for city in range(cities):
            dpTable[city][month] = 99999 #I gave a max number
            for perCity in range(cities):
                if ((dpTable[perCity][month - 1] + relocationCost[perCity][city]) < dpTable[city][month]):
                    dpTable[city][month] = dpTable[perCity][month - 1] + relocationCost[perCity][city]
                    path[city][month] = perCity
            dpTable[city][month] += operatingCost[city][month]
        month += 1

    min = float('inf')
    for c in range(cities):
        if (dpTable[c][months - 1] < min):
            min = dpTable[c][months - 1]

    print("Cost is", min)
#MAIN
cities = 2
months = 4
operatingCost = [[1, 3, 20, 30],
                 [50, 20, 2, 4]]

relocationCost = [[0, 10], #2 sehir arasinda gidip gelme costu
                  [10, 0]]

findCost(cities, months, operatingCost, relocationCost)