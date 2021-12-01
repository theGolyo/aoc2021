with open('input') as input:
    lines = [int(line) for line in input.readlines()]

prevDepthSum = lines[0] + lines[1] + lines[2]
increaseCount = 0
for i in range(1, len(lines) - 2):
    depthSum = lines[i] + lines[i+1] + lines[i+2] 
    if depthSum > prevDepthSum:
        increaseCount += 1
    prevDepthSum = depthSum

print(increaseCount)
