with open('input') as input:
    input = [list(int(i) for i in line.strip()) for line in input.readlines()]


def getNeighbours(i, j):
    coords = []
    if i > 0:
        coords.append((i - 1, j))
    if j > 0:
        coords.append((i, j - 1))
    if i < SIZE - 1:
        coords.append((i + 1, j))
    if j < SIZE- 1:
        coords.append((i, j + 1))
    return coords


def getMinRiskPoint():
    min = float("infinity")
    minP = (-1, -1)
    for p in visited:
        if riskMap[p] < min:
            min = riskMap[p]
            minP = p
    return minP

def getDist(i, j):
    rowOffset = int(i / INPUT_SIZE)
    colOffset = int(j / INPUT_SIZE)
    return (input[i % INPUT_SIZE][j % INPUT_SIZE] + colOffset + rowOffset - 1) % 9 + 1

riskMap = dict()
unsureRisk = dict()
prevVertex = dict()
visited = dict()
enterCost = []
INPUT_SIZE = len(input)
SIZE = INPUT_SIZE * 5
for i in range(SIZE):
    enterCost.append([])
    for j in range(SIZE):
        enterCost[i].append(getDist(i, j))
        riskMap[(i, j)] = float("infinity")
        unsureRisk[(i, j)] = True
riskMap[(0, 0)] = 0
visited[(0,0)] = True
target = (SIZE - 1, SIZE - 1)
while len(unsureRisk) > 0:
    minP = getMinRiskPoint()
    if minP == target:
        break
    del unsureRisk[minP]
    del visited[minP]
    for n in getNeighbours(*minP):
        if n in unsureRisk:
            dist = enterCost[n[0]][n[1]]
            newRisk = riskMap[minP] + dist
            visited[n] = True
            if newRisk < riskMap[n]:
                riskMap[n] = newRisk
                prevVertex[n] = minP

# target = (SIZE - 1, SIZE - 1)

# path = [target]
# while path[-1] in prevVertex:
#     path.append(prevVertex[path[-1]])
print(riskMap[target])
