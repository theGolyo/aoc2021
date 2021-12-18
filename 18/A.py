with open('input') as input:
    input = [i.strip() for i in input.readlines()]

def createEmptyNode():
    return {"value": None, "left": None, "right": None, "parent": None, "depth": 0}

def convertToTree(inpStr):
    root = None
    nodePointer = None
    for s in inpStr:
        if s == "[":
            if root == None:
                root = createEmptyNode()
                nodePointer = root
            else:
                child = createEmptyNode()
                child["parent"] = nodePointer
                child["depth"] = nodePointer["depth"] + 1

                if nodePointer["left"] == None:
                    nodePointer["left"] = child
                else:
                    nodePointer["right"] = child
                nodePointer = child

        elif s in [str(i) for i in range(10)]:
            child = createEmptyNode()
            child["value"] = int(s)
            child["parent"] = nodePointer
            child["depth"] = nodePointer["depth"] + 1

            if nodePointer["left"] == None:
                nodePointer["left"] = child
            else:
                nodePointer["right"] = child
        elif s == "]":
            nodePointer = nodePointer["parent"]
    return root

def treeToString(tree):
    if tree == None:
        return ""
    if isLeaf(tree):
        return str(tree["value"])
    return "[" + treeToString(tree["left"]) + "," + treeToString(tree["right"]) + "]"

def isLeaf(node):
    return node["left"] == None and node["right"] == None

def findExplodePair(node):
    if node == None:
        return None
    left = findExplodePair(node["left"])
    if left:
        return left
    right = findExplodePair(node["right"])
    if right:
        return right
    if node["depth"] >= 4 and not isLeaf(node):
        return node
    return None

def explode(pairNode):
    leftVal = pairNode["left"]["value"]
    rightVal = pairNode["right"]["value"]
    pairNode["left"] = None
    pairNode["right"] = None
    pairNode["value"] = 0

    parent = pairNode["parent"]
    child = pairNode
    while parent != None:
        if parent["left"] is not child:
            leaf = findRightmostLeaf(parent["left"])
            leaf["value"] += leftVal
            break
        else:
            child = parent
            parent = parent["parent"]

    parent = pairNode["parent"]
    child = pairNode
    while parent != None:
        if parent["right"] is not child:
            leaf = findLeftmostLeaf(parent["right"])
            leaf["value"] += rightVal
            break
        else:
            child = parent
            parent = parent["parent"]

def findRightmostLeaf(tree):
    if isLeaf(tree):
        return tree
    elif tree["right"] != None:
        return findRightmostLeaf(tree["right"])
    return findRightmostLeaf(tree["left"])

def findLeftmostLeaf(tree):
    if isLeaf(tree):
        return tree
    elif tree["left"] != None:
        return findLeftmostLeaf(tree["left"])
    return findLeftmostLeaf(tree["right"])

def findSplitLeaf(node):
    if node == None:
        return None
    if isLeaf(node):
        if node["value"] > 9:
            return node
        else:
            return None
    left = findSplitLeaf(node["left"])
    if left != None:
        return left
    right = findSplitLeaf(node["right"])
    if right != None:
        return right
    return None

def split(node):
    leftChild = createEmptyNode()
    leftChild["value"] = int(node["value"] / 2)
    leftChild["parent"] = node
    leftChild["depth"] = node["depth"] + 1

    rightChild = createEmptyNode()
    rightChild["value"] = node["value"] - leftChild["value"]
    rightChild["parent"] = node
    rightChild["depth"] = node["depth"] + 1
    node["value"] = None
    node["left"] = leftChild
    node["right"] = rightChild
     
def reduce(tree):
    reduced = False
    if findExplodePair(tree) != None:
        reduced = True
        explode(findExplodePair(tree))
    elif findSplitLeaf(tree) != None:
        reduced = True
        split(findSplitLeaf(tree))
    if reduced:
        reduce(tree)

def increaseDepth(node):
    if node == None:
        return
    else:
        node["depth"] += 1
        increaseDepth(node["left"])
        increaseDepth(node["right"])

def add(treeOne, treeTwo):
    newRoot = createEmptyNode()
    newRoot["left"] = treeOne
    newRoot["right"] = treeTwo
    treeOne["parent"] = newRoot
    treeTwo["parent"] = newRoot
    increaseDepth(treeOne)
    increaseDepth(treeTwo)
    return newRoot

def magnitude(node):
    if isLeaf(node):
        return node["value"]
    else:
        return 3 * magnitude(node["left"]) + 2 * magnitude(node["right"])

trees = [convertToTree(line) for line in input]
result = trees[0]
for i in range(1, len(trees)):
    result = add(result, trees[i])
    reduce(result)

print(magnitude(result))
