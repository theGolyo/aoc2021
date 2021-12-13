with open('input') as input:
    input = [line.strip() for line in input.readlines()]

folds = []
coords = []
coordsEnded = False
for line in input:
    if line == '':
        coordsEnded = True
    elif coordsEnded:
        if line.find("y") > -1:
            folds.append({"y": int(line.split("y=")[1])})
        if line.find("x") > -1:
            folds.append({"x": int(line.split("x=")[1])})
    else:
        [x, y] = [int(i) for i in line.split(",")]
        coords.append((x, y))

dots = set()
for coord in coords:
    dots.add(coord)

def doFolds():
    endSet = dots
    for fold in folds:
        newSet = set()
        if "y" in fold:
            for coords in endSet:
                if coords[1] > fold["y"]:
                    foldedCoords = (coords[0], coords[1] +
                                    (fold["y"] - coords[1]) * 2)
                    newSet.add(foldedCoords)
                else:
                    newSet.add(coords)
        if "x" in fold:
            for coords in endSet:
                if coords[0] > fold["x"]:
                    foldedCoords = (
                        coords[0] + (fold["x"] - coords[0]) * 2, coords[1])
                    newSet.add(foldedCoords)
                else:
                    newSet.add(coords)
        endSet = newSet
    return endSet

def printDots(dots):
    maxX, maxY = 0, 0
    for p in dots:
        if maxX < p[0]:
            maxX = p[0]
        if maxY < p[1]:
            maxY = p[1]
    for i in range(maxY + 1):
        line = ""
        for j in range(maxX + 1):
            if (j, i) in dots:
                line += "#"
            else:
                line += "."
        print(line)


printDots(doFolds())
