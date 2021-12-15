with open('input') as input:
    input = [line.strip() for line in input.readlines()]

start = input[0]
rules = []
for i in range(2, len(input)):
    rules.append(input[i].split(" -> "))

def countPairFuture(pair, step, char, pairDict):
    if pair not in pairDict:
        pairDict[pair] = dict()
    if not step in pairDict[pair]:
        if step == 0:
            a = 1 if pair[0] == char else 0
            b = 1 if pair[1] == char else 0
            pairDict[pair][step] = a + b
        else:
            insert = getInsert(pair[0], pair[1])
            leftPart = pair[0] + insert
            rightPart = insert + pair[1]
            middlePart = 1 if insert == char else 0
            pairDict[pair][step] = countPairFuture(
                leftPart, step - 1, char, pairDict) + countPairFuture(rightPart, step - 1, char, pairDict) - middlePart
    return pairDict[pair][step]

def getInsert(a, b):
    for rule in rules:
        if rule[0][0] == a and rule[0][1] == b:
            return rule[1]

def countChars(s, step, char):
    pairs = []
    for i in range(len(s) - 1):
        pairs.append(s[i] + s[i+1])
    charDict = dict()
    sum = 0
    for p in pairs:
        sum += countPairFuture(p, step, char, charDict)
    for i in range(1, len(pairs)):
        if pairs[i][0] == char:
            sum -= 1
    return sum


charSet = set()
for char in start:
    charSet.add(char)

max = 0
min = float("infinity")
for char in charSet:
    sum = countChars(start, 40, char)
    if sum > max:
        max = sum
    if sum < min:
        min = sum
print(max - min)
