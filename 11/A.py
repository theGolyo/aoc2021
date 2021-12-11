with open('input') as input:
    octo = [[int(s) for s in list(line.strip())] for line in input.readlines()]

def getNeighbours(i, j):
    neighbours = []
    if i > 0:
        neighbours.append([i - 1, j])
    if j > 0:
        neighbours.append([i, j - 1])
    if i < len(octo) - 1:
        neighbours.append([i + 1, j])
    if j < len(octo[i]) - 1:
        neighbours.append([i, j+1])
    if i > 0 and j > 0:
        neighbours.append([i - 1, j - 1])
    if i > 0 and j < len(octo) - 1:
        neighbours.append([i - 1, j + 1])
    if i < len(octo) - 1 and j > 0:
        neighbours.append([i+1, j - 1])
    if i < len(octo) - 1 and j < len(octo[i]) - 1:
        neighbours.append([i+1, j+1])
    return neighbours

def step():
    flashed = []
    for i in range(len(octo)):
        for j in range(len(octo[i])):
            octo[i][j] += 1

    active = True
    while active:
        active = False
        for i in range(len(octo)):
            for j in range(len(octo[i])):
                if octo[i][j] > 9 and [i, j] not in flashed:
                    active = True
                    flashed.append([i, j])
                    n = getNeighbours(i, j)
                    for p in n:
                        octo[p[0]][p[1]] += 1
    for p in flashed:
        octo[p[0]][p[1]] = 0
    return len(flashed)

sum = 0
for i in range(100):
    sum += step()

print(sum)