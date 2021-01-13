#command line arguments: 1 - input file name; 2 - output file name; 
# 3 - debug printing preferance (1 for on, otherwise off)

import sys

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
if len(sys.argv) > 3:
    debug = int(sys.argv[3])
else:
    debug = 0

#debug print statements
def printd(args):
    if debug == 1:
        for arg in args:
            print(arg, end="")

#handle input file
fileHandler = open(INPUT_FILE)
lines = fileHandler.readlines()
fileHandler.close()

#store input file contents in 2D array
grid = []
fill_index = 0
for line in lines:
    grid.append([])
    vals = line.split()
    for val in vals:
        grid[fill_index].append(val)
    fill_index += 1

#verify valid input 
if len(grid) == 1 and len(grid[0]) == 1 and grid[0] == []:
    sys.exit("no information recieved from input file")

width = len(grid[0])
printd(["width: ", width, "\n\n"])
for line in grid:
    printd(["line len: ",  len(line), "\n"])
    if len(line) != width:
        sys.exit("lines are of unequal size in starting grid")

#debugging
printd(["\nSTARTING GRID:", "\n\n"])
for line in grid:
    for element in line:
        printd([element, " "])
    printd("\n")

#bounds of traversal
LAST_ROW = len(grid) - 1
LAST_COLUMN = width - 1

#helper functions
def in_range(x,y):
    return x < LAST_COLUMN and x >=0 and y < LAST_ROW and y >=0

#initialize a grid with 0 at holes and -1 for everything else
dis_grid = []
for i in range(len(grid)):
    dis_grid.append([])
    for j in range(width):
        if grid[i][j] == '@':
            dis_grid[i].append(0)
        else:
            dis_grid[i].append(-1)

#debugging
printd(["\nBEFORE TRAVERSAL:", "\n\n"])
for line in dis_grid:
    for element in line:
        printd([element, " "])
    printd("\n")

#fill a queue with all holes
q = []
for row in range(len(dis_grid)):
    for col in range(len(line)):
        if dis_grid[row][col] == 0:
            q.append([row,col])

#debugging
printd(["\nHOLES: "])
for item in q:
    printd([item])
printd(["\n\n"])

#helper function - check adjacent squares
def ck_adj(row,col):
    row_adjust = [0,-1,0,1]
    col_adjust = [-1,0,+1,0]
    for i in range(4):
        ck_row = row + row_adjust[i]
        ck_col = col + col_adjust[i]
        if ck_row >= 0 and ck_col >= 0 and ck_row < LAST_ROW+1 and ck_col < LAST_COLUMN+1 and grid[ck_row][ck_col] == 'O' and (dis_grid[ck_row][ck_col] < 0 or dis_grid[ck_row][ck_col] > dis_grid[row][col]+1):
            dis_grid[ck_row][ck_col] = dis_grid[row][col] + 1
            q.append([ck_row,ck_col])
            

#add to adjacent squares acordingly when not walls and keep going until queue is empty
while len(q) > 0:
    ck_adj(q[0][0],q[0][1])
    q.remove(q[0])

#debugging
printd(["\nAFTER TRAVERSAL:", "\n\n"])
for line in dis_grid:
    for element in line:
        printd([element, " "])
    printd("\n")

#write results to file
fileHandler = open(OUTPUT_FILE, 'w')
for row in dis_grid:
    for col in range(LAST_COLUMN):
        fileHandler.write(str(row[col]))
        if col != LAST_COLUMN:
            fileHandler.write(" ")
    fileHandler.write("\n")