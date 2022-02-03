
board = [
   ['6','1','5','7',' ',' ',' ','4',' ',],
   ['9',' ',' ','5',' ','2',' ',' ','3',],
   [' ',' ',' ',' ','6',' ',' ','5',' ',],
   [' ',' ','8','6',' ',' ',' ',' ',' ',],
   [' ',' ','1','9',' ','5','3',' ','8',],
   [' ',' ','7',' ',' ','1','5',' ',' ',],
   [' ',' ','9',' ','8',' ','4','7','1',],
   [' ','4','3',' ',' ','7',' ','8','5',],
   [' ','8',' ',' ',' ','4','9','3',' ',],
]

plan = []
all_elems = []
remaining = 0

# Count the amount of empty cells on the board.
for y in range(0, board.__len__()):
    for x in range(0, board[y].__len__()):
        if (board[y][x] == ' '):
            remaining += 1

# Create array of all numbers. This will reduce the complexity of the following loop.
for i in range(1,10):
    all_elems.append(str(i))

# Generate full plan with all moves enabled. Once updatePlan() is called, all impossible moves will be purged.
for y in range(0,9):
    line = []
    for x in range(0,9):
        line.append(all_elems.copy())
    plan.append(line)

# Return the box which this coordinate is contained.
def getBox(x, y):
    boxX = 0
    boxY = 0

    if x > 2:
        boxX += 1
    if x > 5:
        boxX += 1
    if y > 2:
        boxY += 1
    if y > 5:
        boxY += 1

    return boxX, boxY

# Return all numbers contained within the a box. Each box is 3x3, which means there are 3x3 boxes on the board.
def getNumsInBox(boxX, boxY):
    nums = []

    for y in range(0 + 3 * boxY, 3 + 3 * boxY):
        for x in range(0 + 3 * boxX,3 + 3 * boxX):
            found = board[y][x]
            if found != ' ' and not found in nums:
                nums.append(found)

    return nums

# Writes the current planning in the console. Resource intensive function!
def printPlan():
    for i in range(0, plan.__len__()):
        print('Row', i)
        item = plan[i]
        for j in range(0, item.__len__()):
            print("\t", item[j])
        print('')

# Writes the current board in the console. Resource intensive function!
def printBoard():
    print('|-----------------|')
    for y in range(0, board.__len__()):
        line = board[y]
        print('|', end = '')
        for x in range(0, line.__len__()):
            x_sep = ' '
            if (x+1) % 3 == 0 and x != 0:
                x_sep = '|'
            print(line[x], end = x_sep)
        print('')
        if y != 0 and (y+1) % 3 == 0:
            print('|-----------------|')

# Re-calculate the plan by re-iterating through the board to determine all remaining possible moves.
def updatePlan():
    for select_y in range(0, plan.__len__()):
        for select_x in range(0, plan[select_y].__len__()):
            selected = board[select_y][select_x]
            if selected != ' ': # Already used up
                plan[select_y][select_x] = []
            else:
                # search along x and y axises
                for search_x in range(0, board[select_y].__len__()):
                    found = board[select_y][search_x]
                    if found in plan[select_y][select_x]:
                        plan[select_y][select_x].remove(found)
                for search_y in range(0, board.__len__()):
                    found = board[search_y][select_x]
                    if found in plan[select_y][select_x]:
                        plan[select_y][select_x].remove(found)
                # search inside local box
                boxX, boxY = getBox(select_x, select_y)
                #print("Found box", boxX, "from", select_x)
                boxNums = getNumsInBox(boxX, boxY)
                for num in boxNums:
                    if num in plan[select_y][select_x]:
                        plan[select_y][select_x].remove(num)

# Search for the first plan that shows up and apply it to the board at relative position.
def makeMoves():
    for y in range(0, plan.__len__()):
        for x in range(0, plan[y].__len__()):
            selectedPlan = plan[y][x];
            if selectedPlan.__len__() == 1:
                board[y][x] = selectedPlan[0]
                print("Played", selectedPlan[0], "at", x, y)
                return True
    return False

printBoard()
updatePlan()
while makeMoves(): # -- MAIN LOOP --
    remaining -= 1
    print("Remaining, ", remaining)
    updatePlan()
    printBoard()

printBoard()
if remaining > 0:
    printPlan()