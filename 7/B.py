with open('input') as input:
    inputStr = input.readline()

positions = [int(time) for time in inputStr.split(",")]
minPos = min(positions)
maxPos = max(positions)

def fuelCalc(dist):
    return (dist * (dist + 1)) / 2

smallestDist = -1
for i in range(minPos, maxPos + 1):
    distSum = 0
    for pos in positions:
        fuel = fuelCalc(abs(pos - i))
        distSum += fuel
    if smallestDist > distSum or smallestDist == -1:
        smallestDist = distSum
print(int(smallestDist))
    