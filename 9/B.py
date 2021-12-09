with open('input') as input:
    heights = [list(line.strip()) for line in input.readlines()]

def getNeighbours(i, j):
    neighbours = []
    if i > 0:
        neighbours.append([i-1,j])
    if j > 0:
        neighbours.append([i,j - 1])
    if i < len(heights) - 1:
        neighbours.append([i+1,j])
    if j < len(heights[i]) - 1:
        neighbours.append([i,j+1])
    return neighbours

def isLowPoint(i, j):
    value = int(heights[i][j])
    neighbours = getNeighbours(i, j)
    for p in neighbours:
        if value >= int(heights[p[0]][p[1]]):
            return False
    return True

def createBasin(i, j, basin):
    basin.append([i, j])
    neighbours = getNeighbours(i, j)
    for p in neighbours:
        if p not in basin and int(heights[p[0]][p[1]]) != 9:
            createBasin(p[0], p[1], basin)
    return basin

basinSizes = []
for i in range(len(heights)):
    for j in range(len(heights[i])):
        if isLowPoint(i, j):
            basinSizes.append(len(createBasin(i, j, [])))
basinSizes.sort()
print(basinSizes[-1]*basinSizes[-2]*basinSizes[-3])

