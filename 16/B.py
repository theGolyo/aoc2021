with open('input') as input:
    input = [i.strip() for i in input.readlines()]


def hexToBits(hexChar):
    if hexChar == "0":
        return "0000"
    elif hexChar == "1":
        return "0001"
    elif hexChar == "2":
        return "0010"
    elif hexChar == "3":
        return "0011"
    elif hexChar == "4":
        return "0100"
    elif hexChar == "5":
        return "0101"
    elif hexChar == "6":
        return "0110"
    elif hexChar == "7":
        return "0111"
    elif hexChar == "8":
        return "1000"
    elif hexChar == "9":
        return "1001"
    elif hexChar == "A":
        return "1010"
    elif hexChar == "B":
        return "1011"
    elif hexChar == "C":
        return "1100"
    elif hexChar == "D":
        return "1101"
    elif hexChar == "E":
        return "1110"
    elif hexChar == "F":
        return "1111"


def convert(packet):
    bitString = ""
    for hex in packet:
        bitString += hexToBits(hex)
    return bitString


def parse(bitStr, start):
    packetType = int(bitStr[start+3:start+6], 2)
    if packetType == 4:
        # literal value
        valueBits = ""
        offset = start+6
        end = False
        while not end:
            end = bitStr[offset] == "0"
            valueBits += bitStr[(offset+1):(offset+5)]
            offset += 5
        packetLength = offset-start
        return (packetLength, int(valueBits, 2))
    else:
        # operator
        lengthType = int(bitStr[start+6])
        subPacketValues = []
        if lengthType == 0:
            bitLength = int(bitStr[start+7:start+22], 2)
            nextPacketStart = start + 22
            while nextPacketStart < start + 22 + bitLength:
                (packetLength, subPacketValue) = parse(bitStr, nextPacketStart)
                nextPacketStart += packetLength
                subPacketValues.append(subPacketValue)
            packetLength = nextPacketStart - start
            return (packetLength, calculateWithType(subPacketValues, packetType))
        else:
            packetNumber = int(bitStr[start+7:start+18], 2)
            nextPacketStart = start + 18
            count = 0
            while count < packetNumber:
                count += 1
                (packetLength, subPacketValue) = parse(bitStr, nextPacketStart)
                nextPacketStart += packetLength
                subPacketValues.append(subPacketValue)
            packetLength = nextPacketStart - start
            return (packetLength, calculateWithType(subPacketValues, packetType))

def calculateWithType(packetValues, type):
    if type == 0:
        return sum(packetValues)
    elif type == 1:
        product = 1
        for v in packetValues:
            product *= v
        return product
    elif type == 2:
        return min(packetValues)
    elif type == 3:
        return max(packetValues)
    # elif type == 4:
    #     return packetValues[0]
    elif type == 5:
        return 1 if packetValues[0] > packetValues[1] else 0
    elif type == 6:
        return 1 if packetValues[0] < packetValues[1] else 0
    elif type == 7:
        return 1 if packetValues[0] == packetValues[1] else 0

for packet in input:
    bitStr = convert(packet)
    (length, value) = parse(bitStr, 0)
    print(value)
