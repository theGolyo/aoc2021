with open('input') as input:
    edges = [line.strip() for line in input.readlines()]

adjList = dict()

for edge in edges:
    [f, t] = edge.split("-")
    if not f in adjList:
        adjList[f] = []
    if not t in adjList:
        adjList[t] = []
    adjList[f].append(t)
    if t != "start":
        adjList[f].append(t)
    if f != "start":
        adjList[t].append(f)


def isSmall(c):
    return c.upper() != c


def findPaths(node, prev, visited):
    if node == "end":
        prev += "end"
        # print(prev)
        return 1
    prev += node + ","
    if node in visited:
        return 0
    if isSmall(node):
        visited.add(node)
    count = 0
    for n in adjList[node]:
        visCopy = visited.copy()
        count += findPaths(n, prev, visCopy)
    return count


def start():
    count = findPaths("start", "", set())
    print(count)


start()
