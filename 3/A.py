with open('input') as input:
    lines = [line.strip() for line in input.readlines()]

gammaStr = ''
epsilonStr = ''
limit = len(lines) / 2
bitNumInPos = len(lines[0])
for i in reversed(range(bitNumInPos)):
    zeroCount = 0
    oneCount = 0
    for line in lines:
        pos = int(line, 2)
        bit = pos & (1 << i)
        if bit == 0:
            zeroCount += 1
        else:
            oneCount += 1
        if zeroCount > limit:
            gammaStr += '0'
            epsilonStr += '1'
            break
        elif oneCount > limit:
            gammaStr += '1'
            epsilonStr += '0'
            break
gamma = int(gammaStr, 2)
epsilon = int(epsilonStr, 2)
print(gamma* epsilon)
