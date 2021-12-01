with open('input') as input:
    lines = [int(line) for line in input.readlines()]

prevDepth = lines[0]
increaseCount = 0
for depth in lines:
    if depth > prevDepth:
        increaseCount += 1
    prevDepth = depth

print(increaseCount)
