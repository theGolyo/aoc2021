with open('input') as input:
    input = [list(int(i) for i in line.strip()) for line in input.readlines()]


def getNeighbours(i, j):
    coords = []
    if i > 0:
        coords.append((i-1, j))
    if j > 0:
        coords.append((i, j - 1))
    if i < SIZE - 1:
        coords.append((i+1, j))
    if j < SIZE - 1:
        coords.append((i, j+1))
    return coords


def getMinRiskPoint():
    min = float("infinity")
    minP = (-1, -1)
    for p in unsureRisk:
        if riskMap[p] < min:
            min = riskMap[p]
            minP = p
    return minP


riskMap = dict()
unsureRisk = []
prevVertex = dict()

SIZE = len(input)
for i in range(SIZE):
    for j in range(SIZE):
        riskMap[(i, j)] = float("infinity")
        unsureRisk.append((i, j))
riskMap[(0, 0)] = 0

while len(unsureRisk) > 0:
    minP = getMinRiskPoint()
    unsureRisk.remove(minP)
    for n in getNeighbours(*minP):
        if n in unsureRisk:
            dist = input[n[0]][n[1]]
            newRisk = riskMap[minP] + dist
            if newRisk < riskMap[n]:
                riskMap[n] = newRisk
                prevVertex[n] = minP

target = (SIZE - 1, SIZE - 1)
# path = [target]
# while path[-1] in prevVertex:
#     path.append(prevVertex[path[-1]])
print(riskMap[target])
