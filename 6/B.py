with open('input') as input:
    inputStr = input.readline()

fishTimers = [int(time) for time in inputStr.split(",")]

days = 256
descendantCountMap = dict()


def countDescendants(daysLeft):
    if daysLeft in descendantCountMap:
        return descendantCountMap[daysLeft]
    if (daysLeft < 7):
        descendantCountMap[daysLeft] = 1
    else:
        descendantCountMap[daysLeft] = countDescendants(daysLeft - 7) + countDescendants(daysLeft - 9)
    return descendantCountMap[daysLeft]


sum = 0
for time in fishTimers:
    sum += countDescendants(days + 6 - time)

print(sum)
