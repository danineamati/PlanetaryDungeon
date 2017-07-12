import random

rows = 6 - 2
columns = 6

Column_list = [] #Combination of rows to make the array
Column_identifier = []

def setBoardLocation(rowcolumn, item_type):
    print "Which", str(rowcolumn), "would you like your", str(item_type), "?"
    location = raw_input()
    print "You have set your", str(item_type), "at", str(rowcolumn), str(location)
    return int(location)

def printBoard(Column_identifier, Column_list):
    print ""
    #Print the grid
    print "x", Column_identifier
    for row in range(len(Column_list)):
        print row, Column_list[row]

#Set up the lists
for row in range(rows):
    Column_list.append(["O"] * columns) #O for Open

for column in range(columns + 1):
    Column_identifier.append(str(column))

printBoard(Column_identifier, Column_list)

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
Boss_row = setBoardLocation("row", "Boss")
Boss_column = setBoardLocation("column", "Boss")

Column_list[Boss_row][Boss_column] = "B"

printBoard(Column_identifier, Column_list)

print "Let's set your first wall!"
#Set Wall Location
Wall1_row = setBoardLocation("row", "Wall") #Note the 1 (one) not l
Wall1_column = setBoardLocation("column", "Wall")

if Wall1_row != Boss_row or Wall1_column != Boss_column:
    Column_list[Wall1_row][Wall1_column] = "W"
else:
    print "That spot is already taken!"
    Wall1_row = setBoardLocation("row", "Wall") #Again, note the 1 (one) not l
    Wall1_column = setBoardLocation("column", "Wall")

printBoard(Column_identifier, Column_list)
