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
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def parseLine(line):
    stack = []
    p = 0
    for s in line:
        if s in opening:
            stack.append(s)
        else:
            if stack[-1] != closing[s]:
                p = score[s]
                return p
            else:
                stack.pop()
    return p


s = 0
for line in lines:
    s += parseLine(line)

print(s)
