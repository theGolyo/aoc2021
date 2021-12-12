with open('testinput1') as input:
    edges = [line.strip() for line in input.readlines()]

adjList = dict()

for edge in edges:
    [f, t] = edge.split("-")
    if not f in adjList:
        adjList[f] = []
    if not t in adjList:
        adjList[t] = []
    
    if t != "start":
        adjList[f].append(t)
    if f != "start":
        adjList[t].append(f)

def isSmall(c):
    return c.upper() != c


def findPaths(node, pathStr, visited, doubleVisitUsed):
    if node == "end":
        pathStr += "end"
        # print(pathStr)
        return 1
    pathStr += node + ","

    if node in visited and doubleVisitUsed:
        return 0

    count = 0
    if node in visited:
        # double
        for n in adjList[node]:
            count += findPaths(n, pathStr, visited, True)
    else:
        if isSmall(node):
            visited = set(visited)
            visited.add(node)
        for n in adjList[node]:
            count += findPaths(n, pathStr, visited, doubleVisitUsed)
    return count


def start():
    count = findPaths("start", "", set(), False)
    print(count)


start()
