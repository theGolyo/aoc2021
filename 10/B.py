with open('input') as input:
    lines = [list(line.strip()) for line in input.readlines()]

opening = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

closing = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

score = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def parseLine(line):
    stack = []
    missing = []
    for s in line:
        if s in opening:
            stack.append(s)
        else:
            if stack[-1] != closing[s]:
                # corrupted
                return missing
            else:
                stack.pop()
    if (len(stack) != 0):
        for s in stack[::-1]:
            missing.append(opening[s])
    return missing

def calcScore(missing):
    sum = 0
    for s in missing:
        sum *= 5
        sum += score[s]
    return sum


scores = []
for line in lines:
    missing = parseLine(line)
    if (len(missing) > 0):
        scores.append(calcScore(missing))

scores.sort()
print(scores[int(len(scores) / 2)])
        

