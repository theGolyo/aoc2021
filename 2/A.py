with open('input') as input:
    lines = [line.split(' ') for line in input.readlines()]

depth = 0
horizontal = 0

for line in lines:
    direction = line[0]
    delta = int(line[1])
    if direction == 'forward':
        horizontal += delta
    elif direction == 'down':
        depth += delta
    else:
        # up
        depth -= delta

print(depth * horizontal)