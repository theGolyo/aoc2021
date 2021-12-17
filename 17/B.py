with open('input') as input:
    input = input.readline().split(", ")

rect = [
    int(input[0].split("x=")[1].split("..")[0]),
    int(input[0].split("x=")[1].split("..")[1]),
    int(input[1].split("y=")[1].split("..")[0]),
    int(input[1].split("y=")[1].split("..")[1]),
]

def simulateX(vx):
    x = 0
    stepCount = 0
    range = [-1,-1]
    hit = False
    while vx > 0:
        stepCount += 1
        x += vx
        vx = max(vx - 1, 0)
        if x >= rect[0]:
            if x <= rect[1]:
                # in
                hit = True
                if range[0] == -1:
                    range[0] = stepCount
                range[1] = stepCount if vx > 0 else float("infinity")
            else:
                # overshoot
                return {"hit": hit, "range": range}
    return {"hit": hit, "range": range}

def simulateY(vy):
    y = 0
    stepCount = 0
    range = [-1,-1]
    hit = False
    while True:
        stepCount += 1
        y += vy
        vy -= 1
        if y <= rect[3]:
            if y >= rect[2]:
                # in
                hit = True
                if range[0] == -1:
                    range[0] = stepCount
                range[1] = stepCount
            else:
                # overshoot
                return {"hit": hit, "range": range}

def find_min_vx():
    vx = 0
    hit = False
    while not hit:
        vx += 1
        hit = simulateX(vx)["hit"]
    return vx

def find_possible_vy_list():
    hitList = []
    vy = min_vy
    while vy <= max_vy:
        simulationResult = simulateY(vy)
        if simulationResult["hit"]:
            hitList.append((vy, simulationResult["range"]))
        vy += 1
    return hitList

def find_possible_vx_list():
    hitList = []
    vx = min_vx
    while vx <= max_vx:
        simulationResult = simulateX(vx)
        if simulationResult["hit"]:
            hitList.append((vx, simulationResult["range"]))
        vx += 1
    return hitList

min_vy = rect[2]
max_vy = (-1 * (rect[2] + 1))

min_vx = find_min_vx()
max_vx = rect[1]


vy_list = find_possible_vy_list()
vx_list = find_possible_vx_list()
possible_velocities = []

def overlap(a, b):
    return not a[1] < b[0] and not a[0] > b[1] 

for vx_info in vx_list:
    for vy_info in vy_list:
        xr = vx_info[1]
        yr = vy_info[1]
        if overlap(xr, yr):
            possible_velocities.append((vx_info[0], vy_info[0]))

print(len(possible_velocities))
        