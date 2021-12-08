with open('input') as input:
    lines = [line.strip() for line in input.readlines()]

def commonSegments(a, b):
    count = 0
    for i in a:
        if i in b:
            count += 1
    return count

def calcOutput(input, output):
    digitMap = dict()
    for code in input:
        if len(code) == 2:
            digitMap[1] = code
        elif len(code) == 4:
            digitMap[4] = code
        elif len(code) == 3:
            digitMap[7] = code
        elif len(code) == 7:
            digitMap[8] = code

    fiveSegmentNums = list(filter(lambda x: len(x) == 5, input))
    for number in fiveSegmentNums:
        # 3 has three lines in common with 7
        if (commonSegments(digitMap[7], number) == 3):
            digitMap[3] = number
        # 2 has two lines in common with 4
        if (commonSegments(digitMap[4], number) == 2):
            digitMap[2] = number

    # other one five length is 5
    for number in fiveSegmentNums:
        if number != digitMap[2] and number != digitMap[3]:
            digitMap[5] = number

    sixSegmentNums = list(filter(lambda x: len(x) == 6, input))
    for number in sixSegmentNums:
        # 9 contains 3
        if (commonSegments(digitMap[3], number) == 5):
            digitMap[9] = number
        # 6 does not contain 1
        if (commonSegments(digitMap[1], number) == 1):
            digitMap[6] = number
    
    # other one six length is 0
    for number in sixSegmentNums:
        if number != digitMap[9] and number != digitMap[6]:
            digitMap[0] = number

    numStr = ''
    for code in output:
        for i in digitMap:
            if set(digitMap[i]) == set(code):
                numStr += str(i)
                break
    return int(numStr)

sum = 0
for line in lines:
    signalStr, outputStr = [s.strip() for s in line.split("|")]
    signal = signalStr.split(" ")
    output = outputStr.split(" ")
    sum += calcOutput(signal, output)
print(sum)