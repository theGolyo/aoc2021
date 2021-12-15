with open('input') as input:
    input = [line.strip() for line in input.readlines()]

start = input[0]
rules = []
for i in range(2, len(input)):
    rules.append(input[i].split(" -> "))


def step(pairStr):
    result = ""
    for i in range(len(pairStr)):
        if i + 1 < len(pairStr):
            insert = checkPair(pairStr[i], pairStr[i + 1])
            result += pairStr[i] + insert
        else:
            result += pairStr[i]
    return result


def checkPair(a, b):
    for rule in rules:
        if rule[0][0] == a and rule[0][1] == b:
            return rule[1]
    return ""


polymerStr = start
for i in range(10):
    polymerStr = step(polymerStr)

occurence = dict()
for c in polymerStr:
    if c in occurence:
        occurence[c] += 1
    else:
        occurence[c] = 1

max = 0
min = len(polymerStr)
for c in occurence:
    if occurence[c] > max:
        max = occurence[c]
    if occurence[c] < min:
        min = occurence[c]
print(max - min)
