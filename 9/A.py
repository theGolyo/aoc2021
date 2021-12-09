with open('input') as input:
    heights = [list(line.strip()) for line in input.readlines()]

def isLowPoint(i, j):
    value = int(heights[i][j])
    neighbours = []
    if i > 0:
        neighbours.append(heights[i-1][j])
    if j > 0:
        neighbours.append(heights[i][j - 1])
    if i < len(heights) - 1:
        neighbours.append(heights[i+1][j])
    if j < len(heights[i]) - 1:
        neighbours.append(heights[i][j+1])
    for p in neighbours:
        if value >= int(p):
            return False
    return True

sum = 0
for i in range(len(heights)):
    for j in range(len(heights[i])):
        if isLowPoint(i, j):
            risk = int(heights[i][j]) + 1
            sum += risk
print(sum)
