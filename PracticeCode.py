import random

rows = 6 - 2
columns = 6

Row_list = [] #List corresponding with each row
Column_list = [] #Combination of rows to make the array

#Set up the lists
for column in range(columns):
    Row_list.append("O") #O for Open

for row in range(rows):
    Column_list.append(Row_list)

for row in range(len(Column_list)):
    print Column_list[row]

#Set borders
#The first and last index of Row_list needs to be walls
for column in range(1):
    Column_list[0].pop()
    Column_list[0].insert(0, "X")
    Column_list[0].append("X")

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

print ""
#Print the grid
for row in range(len(Column_list)):
    print Column_list[row]
