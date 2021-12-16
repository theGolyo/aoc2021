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
    version = int(bitStr[start:start+3], 2)
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
        return (version, packetLength)
    else:
        # operator
        lengthType = int(bitStr[start+6])
        versionSum = version
        if lengthType == 0:
            bitLength = int(bitStr[start+7:start+22], 2)
            nextPacketStart = start + 22
            while nextPacketStart < start + 22 + bitLength:
                (v, packetLength) = parse(bitStr, nextPacketStart)
                nextPacketStart += packetLength
                versionSum += v
            packetLength = nextPacketStart - start
            return (versionSum, packetLength)
        else:
            packetNumber = int(bitStr[start+7:start+18], 2)
            nextPacketStart = start + 18
            count = 0
            while count < packetNumber:
                count += 1
                (v, packetLength) = parse(bitStr, nextPacketStart)
                nextPacketStart += packetLength
                versionSum += v
            packetLength = nextPacketStart - start
            return (versionSum, packetLength)

for packet in input:
    bitStr = convert(packet)
    (versionSum, length) = parse(bitStr, 0)
    print(versionSum)
