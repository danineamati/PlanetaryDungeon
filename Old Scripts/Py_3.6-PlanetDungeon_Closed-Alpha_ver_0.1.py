import random

rows = 5
columns = 5 + 1

Column_list = [] #Combination of rows to make the array
Column_identifier = []

def setBoardLocation(rowcolumn, item_type, rowscolumnsindex):
    locationset = False
    while locationset == False:
        print("Which", str(rowcolumn), "would you like your", str(item_type), "?")
        location = int(input())
        if location > 0 and location <= rowscolumnsindex:
            print("You have set your", str(item_type), "at", str(rowcolumn), str(location))
            return int(location)
            locationset = True
        else:
            print("This location is not on the board. Try another location.")

def printBoard(Column_identifier, Column_list):
    print("")
    #Print the grid
    print("x", Column_identifier)
    for row in range(len(Column_list)):
        print(row, Column_list[row])

def setWall(Column_list, columns, rows):
    wallset = False
    while wallset == False:
        Wall_column = setBoardLocation("column", "Wall", columns)
        Wall_row = setBoardLocation("row", "Wall", rows)
        if Column_list[Wall_row][Wall_column] == "W" or \
           Column_list[Wall_row][Wall_column] == "X" or \
           Column_list[Wall_row][Wall_column] == "S":
            print("There is already a Wall there! Try another location.")
        elif Wall_row != Boss_row or Wall_column != Boss_column:
            Column_list[Wall_row][Wall_column] = "W"
            wallset = True
        else:
            print("That spot is already taken! Try another location")

#Set up the lists
for row in range(rows):
    Column_list.append(["O"] * columns) #O for Open

for column in range(columns + 1):
    Column_identifier.append(str(column))

#Set borders
#The first and last index of each row needs to be walls
for column in range(rows):
    Column_list[column].pop()
    Column_list[column].insert(0, "X")
    Column_list[column].append("X")

#First Row needs to be all walls
initial_row = []
for column in range(columns + 1):
    initial_row.append("X")
Column_list.insert(0, initial_row) #list from 0 to columns

#Last Index of Column_list needs to be walls
final_row = []
for column in range(columns + 1):
    final_row.append("X")
Column_list.append(final_row) #list from 0 to columns

#Locate the hero starting location
startrow = int(round(rows/2) + 1)
Column_list[startrow][1] = "S"

printBoard(Column_identifier, Column_list)

#Set Boss Location
Boss_column = setBoardLocation("column", "Boss", columns)
Boss_row = setBoardLocation("row", "Boss", rows)

Column_list[Boss_row][Boss_column] = "B"

printBoard(Column_identifier, Column_list)

print("Let's set your first wall!")
#Set Wall Location of first wall
setWall(Column_list, columns, rows)
printBoard(Column_identifier, Column_list)
print("Now try another!")
#Set Wall Location of second wall
setWall(Column_list, columns, rows)
printBoard(Column_identifier, Column_list)


#Path finding algorithm
def AdjacentLoop(Column_identifier, Column_list, Boss_row, Boss_column):
    count = 1
    newpoint = range(5)
    AdjacentList = [[Boss_row, Boss_column, True, False]] #[2] = True correspond to entered
    bossfound = False
    num = 1
    while num < 6 and bossfound == False:
        RunningList = [] #Rooms with adjacent not found; also (re)initialize the list
        RunningIndices = [] #Indices of above rooms; also (re)initialize the list
        for items in range(len(AdjacentList)):
            if AdjacentList[items][3] == False:
                RunningList.append(AdjacentList[items])
                RunningIndices.append(items)
        #print "Adjacent List", AdjacentList, len(AdjacentList)
        #print "Running List", RunningList
        #print "Running Indices", RunningIndices
        #Discover the four adjacent opennings of each new point
        for point in RunningIndices: #Loop through Indices where adjacent rooms are not found yet
            AdjacentList.append([AdjacentList[point][0] + 1, \
                                 AdjacentList[point][1], False, False]) #Append room on right
            AdjacentList.append([AdjacentList[point][0] - 1, \
                                 AdjacentList[point][1], False, False]) #Append room on left
            AdjacentList.append([AdjacentList[point][0], \
                                 AdjacentList[point][1] + 1, False, False]) #Append room above
            AdjacentList.append([AdjacentList[point][0], \
                                 AdjacentList[point][1] - 1, False, False]) #Append room below
            AdjacentList[point][3] = True
            #Check if the the adjacent room is valid
            newpoint = [] #initialize or re-initialize
            #print("newpoint initial", newpoint)
            newpoint = range(len(AdjacentList) - 4, \
                             len(AdjacentList)) #Index of the new four items
            #print("length", len(AdjacentList))
            #print("newpoint", newpoint)
            for new in newpoint:
                #print "new", new
                column =  AdjacentList[new][1] #column coordinate
                row = AdjacentList[new][0] #row coordinate
                #print("row", row, "column", column)
                if Column_list[row][column] == "S": #Start
                    print("The hero has found the boss!")
                    print("Hero traverses", str(count), "rooms.")
                    bossfound = True
                elif Column_list[row][column] == "O": #Check entered criteria
                    #print "Next open point:", AdjacentList[new]
                    Column_list[row][column] = str(count)
                    AdjacentList[new][2] = True
                elif Column_list[row][column] == "X" or Column_list[row][column] == "W": #Check Wall
                    #print("Hit a wall at", AdjacentList[new])
                    pass
                elif Column_list[row][column] == "B": #Check Boss
                    #print("Boss location known")
                    pass
            for index in range(len(AdjacentList)):
                if AdjacentList[len(AdjacentList) - 1][2] == False:
                    AdjacentList.pop(len(AdjacentList) - 1) #remove all invalid rooms
        #print "New Adjacent List", AdjacentList
        printBoard(Column_identifier, Column_list)
        reversed(AdjacentList)
        seen = 0
        for index in range(len(AdjacentList)):
            #print(AdjacentList[seen])
            if AdjacentList[seen][2] == False:
                AdjacentList.pop(len(AdjacentList) - seen) #remove all invalid
                #print "popped"
            else:
                seen += 1
                #print "up one:", seen
        reversed(AdjacentList)
        #print(len(AdjacentList))
        #print AdjacentList
        print("End loop", count)
        count += 1
        num += 1
    print("The hero has found the boss!")
    print("Hero will traverse", str(count - 1), "rooms.")
        
AdjacentLoop(Column_identifier, Column_list, Boss_row, Boss_column)
print("Hero has discovered its intended path!")

#Start Hero movement
def boss_reached(): #This prints the "Boss Reached" interface
    print("The boss has been reached!")

def conditional_adjacent(Column_identifier, Column_list, Checking_row, Checking_column):
    Bossreached = False
    if Column_list[Checking_row][Checking_column] == "B":
        boss_reached()
        return [0, Checking_row, Checking_column]
    elif Column_list[Checking_row][Checking_column].isdigit():
        return [int(Column_list[Checking_row][Checking_column]), Checking_row, Checking_column]
    else:
        return

def check_adjacent(Column_identifier, Column_list, Current_row, Current_column): #This returns the coordinate of the next lowest number
    TileValue = []
    print("Current_row", Current_row)
    print("Current_column", Current_column)
    print("Column_list value", Column_list[Current_row][Current_column])
    Bossreached = False
    #Check Above
    TileValue.append(conditional_adjacent(Column_identifier, Column_list, Current_row - 1, Current_column))
    #Check Right
    TileValue.append(conditional_adjacent(Column_identifier, Column_list, Current_row, Current_column + 1))
    #Check Below
    TileValue.append(conditional_adjacent(Column_identifier, Column_list, Current_row + 1, Current_column))
    #Check Left
    TileValue.append(conditional_adjacent(Column_identifier, Column_list, Current_row, Current_column - 1))
    TileValue = [x for x in TileValue if x!=None]
    TileValue.sort()
    print(TileValue)
    if TileValue[0][0] == 0:
        return ["Boss", TileValue[0][1], TileValue[0][2]]
    return ["next", TileValue[0][1], TileValue[0][2]]

def hero_location(Column_identifier, Column_list): #This updates hero location
    printBoard(Column_identifier, Column_list)

def Hero_Movement(Column_identifier, Column_list, startrow): #This puts the above three functions in one
    initial_location = [int(startrow),1]
    print(initial_location, "row", initial_location[0], initial_location[1])
    #Check adjacent rooms - check_adjacent(Column_identifier, Column_List, Current_row, Current_column)
    #Returns ["Boss"/"next", row, column]
    new_location = check_adjacent(Column_identifier, Column_list, initial_location[0], initial_location[1])
    bossreached = False
    while bossreached == False:
        print(new_location, "New Location")
        if new_location[0] == "Boss":
            print("Hi!")
            bossreached = True
        else:
            new_location = check_adjacent(Column_identifier, Column_list, new_location[1], new_location[2])
        hero_location(Column_identifier, Column_list)
    print("It worked.")

Hero_Movement(Column_identifier, Column_list, startrow)
print("Hero movement complete.")
