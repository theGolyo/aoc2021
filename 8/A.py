with open('input') as input:
    lines = [line.strip() for line in input.readlines()]

digits = {
    0: ["a", "c", "f", "g", "e", "b"],
    1: ["c", "f"],
    2: ["a", "c", "d", "e", "g"],
    3: ["a", "c", "d", "f", "g"],
    4: ["b", "c", "d", "f"],
    5: ["a", "b", "d", "f", "g"],
    6: ["a", "b", "d", "e", "f", "g"],
    7: ["a", "c", "f"],
    8: ["a", "b", "c", "d", "e", "f", "g"],
    9: ["a", "b", "c", "d", "f", "g"],
}

count = 0
for line in lines:
    signalStr, outputStr = [s.strip() for s in line.split("|")]
    signal = signalStr.split(" ")
    output = outputStr.split(" ")
    for code in output:
        if len(code) in [len(digits[1]), len(digits[4]), len(digits[7]), len(digits[8])]:
            count += 1
    
print(count)

