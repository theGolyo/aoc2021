with open('input') as input:
    lines = [line.strip() for line in input.readlines()]

def filterListOGR(list, index):
    if (len(list) == 1):
        return list
    zeroList = []
    oneList = []
    for pos in list:
        bit = pos & (1 << index)
        if bit == 0:
            zeroList.append(pos)
        else:
            oneList.append(pos)
    if len(zeroList) > len(oneList):
        return zeroList
    return oneList

def filterListCOSR(list, index):
    if (len(list) == 1):
        return list
    zeroList = []
    oneList = []
    for pos in list:
        bit = pos & (1 << index)
        if bit == 0:
            zeroList.append(pos)
        else:
            oneList.append(pos)
    if len(oneList) < len(zeroList):
        return oneList
    return zeroList

bitNumInPos = len(lines[0])
posList = [int(line, 2) for line in lines]
ogr = posList
cosr = posList
for i in reversed(range(bitNumInPos)):
    ogr = filterListOGR(ogr, i)
    cosr = filterListCOSR(cosr, i)

print(ogr[0]*cosr[0])



