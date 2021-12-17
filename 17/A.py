with open('input') as input:
    input = input.readline().split(", ")

rect = [
    int(input[0].split("x=")[1].split("..")[0]),
    int(input[0].split("x=")[1].split("..")[1]),
    int(input[1].split("y=")[1].split("..")[0]),
    int(input[1].split("y=")[1].split("..")[1]),
]

max_vy = (-1 * (rect[2] + 1))

def simulate(vy):
    y = 0
    maxY = 0
    while True:
        y += vy
        maxY = max(maxY, y)
        vy -= 1
        if y <= rect[3]:
            if y >= rect[2]:
                # in
                return (True, maxY)
            else:
                # overshoot
                return (False, maxY)

print(simulate(max_vy))
        