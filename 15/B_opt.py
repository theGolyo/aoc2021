import time
# my original solution runs for quite long
# this is a rewrite using Dial's algorithm, a modified Dijsktra's using buckets
with open('input') as input:
    input = [list(int(i) for i in line.strip()) for line in input.readlines()]

start_time = time.perf_counter()
INPUT_SIZE = len(input)
# SIZE = INPUT_SIZE
SIZE = INPUT_SIZE * 5
SOURCE = (0, 0)
TARGET = (SIZE - 1, SIZE - 1) 
def getDist(i, j):
    rowOffset = int(i / INPUT_SIZE)
    colOffset = int(j / INPUT_SIZE)
    return (input[i % INPUT_SIZE][j % INPUT_SIZE] + colOffset + rowOffset - 1) % 9 + 1

cost = []
for i in range(SIZE):
    cost.append([])
    for j in range(SIZE):
        cost[i].append(getDist(i, j))

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

# INIT BUCKETS
# the buckets represent the distance from the source
# the maximum possible distance is width + length steps of cost 9
# to save space we only use a window of buckets, instead of the maximum possible distance to keep the distance from the source
MAX_POSSIBLE_DISTANCE = SIZE * 2 * 9
buckets = [[] for _ in range(10)]

def addToBucket(distance, node):
    buckets[distance % 10].append(node)
def removeFromBucket(distance, node):
    buckets[distance % 10].remove(node)
def getBucket(distance):
    return buckets[distance % 10]

# add the SOURCE to the fist bucket
buckets[0].append(SOURCE)
pathCost = dict()
pathCost[SOURCE] = 0

def dials():
    for i in range(MAX_POSSIBLE_DISTANCE):
        bucket = getBucket(i)
        while len(bucket) > 0:
            next = bucket.pop()
            if next == TARGET:
                return pathCost[next]
            for n in getNeighbours(*next):
                newCost = pathCost[next] + cost[n[0]][n[1]]
                if n in pathCost:
                    if newCost < pathCost[n]:
                        removeFromBucket(pathCost[n], n)
                        pathCost[n] = newCost
                        addToBucket(pathCost[n], n) 
                # neighbour was in "infinity" bucket
                else:
                    pathCost[n] = newCost
                    addToBucket(pathCost[n], n)        

setup_time = time.perf_counter()
print("Setup time:", setup_time - start_time)
print("Result:", dials())
print("Runtime:", time.perf_counter() - setup_time)