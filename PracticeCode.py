import random

rows = 6 - 2
columns = 6

Column_list = [] #Combination of rows to make the array
Column_identifier = []

def setBoardLocation(rowcolumn, item_type, rowscolumnsindex):
    locationset = False
    while locationset == False:
        print "Which", str(rowcolumn), "would you like your", str(item_type), "?"
        location = int(raw_input())
        if location > 0 and location < rowscolumnsindex:
            print "You have set your", str(item_type), "at", str(rowcolumn), str(location)
            return int(location)
            locationset = True
        else:
            print "This location is not on the board. Try another location."

def printBoard(Column_identifier, Column_list):
    print ""
    #Print the grid
    print "x", Column_identifier
    for row in range(len(Column_list)):
        print row, Column_list[row]

def setWall(Column_list, columns, rows):
    wallset = False
    while wallset == False:
        Wall_column = setBoardLocation("column", "Wall", columns)
        Wall_row = setBoardLocation("row", "Wall", rows)
        if Column_list[Wall_row][Wall_column] == "W" or Column_list[Wall_row][Wall_column] == "X":
            print "There is already a Wall there! Try another location."
        elif Wall_row != Boss_row or Wall_column != Boss_column:
            Column_list[Wall_row][Wall_column] = "W"
            wallset = True
        else:
            print "That spot is already taken! Try another location" 

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

printBoard(Column_identifier, Column_list)

#Set Boss Location
Boss_column = setBoardLocation("column", "Boss", columns)
Boss_row = setBoardLocation("row", "Boss", rows)

Column_list[Boss_row][Boss_column] = "B"

printBoard(Column_identifier, Column_list)

print "Let's set your first wall!"
#Set Wall Location of first wall
setWall(Column_list, columns, rows)
printBoard(Column_identifier, Column_list)

print "Now try another!"
#Set Wall Location of second wall
setWall(Column_list, columns, rows)
printBoard(Column_identifier, Column_list)
