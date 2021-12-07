with open('input') as input:
    inputStr = input.readline()

positions = [int(time) for time in inputStr.split(",")]
minPos = min(positions)
maxPos = max(positions)

smallestDist = -1
for i in range(minPos, maxPos + 1):
    distSum = 0
    for pos in positions:
        distSum += abs(pos - i)
    if smallestDist > distSum or smallestDist == -1:
        smallestDist = distSum
print(smallestDist)
    