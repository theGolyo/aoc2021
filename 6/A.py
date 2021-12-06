with open('input') as input:
    inputStr = input.readline()

fishTimers = [int(time) for time in inputStr.split(",")]

days = 80

for i in range(days):
    newFish = []
    for i, time in enumerate(fishTimers):
        if time == 0:
            newFish.append(8)
            fishTimers[i] = 6
        else:
            fishTimers[i] -= 1
    fishTimers.extend(newFish)
            
print(len(fishTimers))