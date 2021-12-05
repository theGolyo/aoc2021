with open('input') as input:
    lines = [line.strip() for line in input.readlines()]

points = {}


def addPoint(x, y):
    if x not in points:
        points[x] = {}
    if y not in points[x]:
        points[x][y] = 0
    points[x][y] += 1


for line in lines:
    start, end = line.split(" -> ")
    startX, startY = [int(p) for p in start.split(",")]
    endX, endY = [int(p) for p in end.split(",")]

    if startX == endX or startY == endY:
        if startX != endX:
            # horizontal
            delta = 1 if startX < endX else -1
            x = startX
            while x != endX:
                addPoint(x, startY)
                x += delta
            addPoint(endX, startY)
        else:
            # vertical
            delta = 1 if startY < endY else -1
            y = startY
            while y != endY:
                addPoint(startX, y)
                y += delta
            addPoint(startX, endY)

count = 0
for x in points:
    for y in points[x]:
        if points[x][y] > 1:
            count += 1

print(count)
