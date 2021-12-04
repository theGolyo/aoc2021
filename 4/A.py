with open('input') as input:
    lines = [line.strip() for line in input.readlines()]

draws = lines[0].split(",")

boards = []
rowIndex = 0
for i in range(1, len(lines)):
    if lines[i] == '':
        newBoard = {'numbers': dict(), 'colHits': dict(), 'rowHits': dict()}
        boards.append(newBoard)
        rowIndex = 0
    else:
        newBoard['rowHits'][rowIndex] = 0
        row = lines[i].replace("  ", " ").split(" ")
        for i, num in enumerate(row):
            boards[-1]['numbers'][num] = {'row': rowIndex, 'col': i}
            if rowIndex == 0:
                newBoard['colHits'][i] = 0
        rowIndex += 1


def play():
    for draw in draws:
        for bingoBoard in boards:
            if draw in bingoBoard['numbers']:
                col = bingoBoard['numbers'][draw]['col']
                row = bingoBoard['numbers'][draw]['row']
                del bingoBoard['numbers'][draw]  # mark number
                bingoBoard['colHits'][col] += 1
                bingoBoard['rowHits'][row] += 1
                if bingoBoard['colHits'][col] == 5 or bingoBoard['rowHits'][row] == 5:
                    # win
                    sum = 0
                    for unmarked in bingoBoard['numbers']:
                        sum += int(unmarked)
                    return sum * int(draw) 
            
print(play())
