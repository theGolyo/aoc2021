with open('input') as input:
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
    adjList[t].append(f)


def isSmall(c):
    return c.upper() != c


def findPaths(node, prev, visited, double):
    if node == "end":
        prev += "end"
        # print(prev)
        return 1
    prev += node + ","

    if node in visited and double:
        return 0

    count = 0
    if node in visited:
        # double
        for n in adjList[node]:
            visCopy = set(visited)
            count += findPaths(n, prev, visCopy, True)
    else:
        if isSmall(node):
            visited.add(node)
        for n in adjList[node]:
            visCopy = set(visited)
            count += findPaths(n, prev, visCopy, double)
    return count


def start():
    count = findPaths("start", "", set(), False)
    print(count)


start()
