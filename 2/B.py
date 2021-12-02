with open('input') as input:
    lines = [line.split(' ') for line in input.readlines()]

depth = 0
horizontal = 0
aim = 0

for line in lines:
    direction = line[0]
    delta = int(line[1])
    if direction == 'forward':
        horizontal += delta
        depth += aim * delta
    elif direction == 'down':
        aim += delta
    else:
        # up
        aim -= delta

print(depth * horizontal)