# Minesweeper
#   > Sets rule of Minesweeper game
#   > Creates gameboard
#   > Both human and machine will interact with rules


# Import other Python files
#   > numpy   necessary for creating two dimensional array
#   > random  generating random numbers for element selection
import numpy as gb
import random


# Create Minesweeper gameboard
#   > r is quantity of row
#   > c is quantity of columns
#   > d is scale of difficulty
#   > Returns the gameboard
def layoutBoard(r, c, d):
  # Dimensions of gameboard  #
  #   > row     is size of gameboard's width
  #   > column  is size of gameboard's length
  row, column = r, c


  #  Difficulty of gameboard
  #   > Difficulty will be a scale based number
  #   > Scale theoretical maximum is determined by gameboard dimensions
  #   > Scale will be between 0 and 9 (a ten point system)
  difficulty = d


  #  Initialize gameboard
  #   > gameboard is a two dimensional array
  #   > all indices that are safe are initialized as 0
  gameboard = gb.full((row, column), 0) 


  #  Station bomb instances
  #   > Stations bombs at random locations
  #   > fields is the quantity of each element of gameboard
  #   > bombScale is the quantity of bombs in ratio to gameboard size
  #   > bombQuantity is the quantity of bombs in the gameboard
  #   > bombCount is the incrementer for the while loop
  #   > while loop will run until each unique field is a bomb
  #   > 1 is bomb, 0 is safe
  fields = row * column
  bombScale = (difficulty + 1) / 10
  bombQuantity = int (fields * bombScale)

  print("Number of bombs:", bombQuantity)

  bombCount = 0
  while (bombCount < bombQuantity):
    x = random.randint(0, row - 1)
    y = random.randint(0, column - 1)
    if gameboard[x][y] != 1:
      gameboard[x][y] = 1
    else:
      bombCount -= 1
    bombCount += 1
  
  
  #  Return gameboard
  #   > Returns constructed gameboard 
  return gameboard


#  ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~  #


# Is the field a bomb
#   > r is location of row
#   > c is location of columns
#   > b is the Minesweeper board
#   > Returns a boolean
def isBomb(r, c, b):
  #  Location of field
  #   > row     is location of x field
  #   > column  is location of y field
  row, column = r, c


  #  Check if bomb
  #   > If bomb return 1
  #   > If safe return 0
  if b[row][column] > 0:
    return 1
  else:
    return 0


#  ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~  #


# Quantity of bombs surrounding field
#   > r is location of row
#   > c is location of columns
#   > b is the Minesweeper board
#   > Returns an two ints (bomb quantity, safe quantity)
def nearField(r, c, b):
  #  Location of field
  #   > row     is location of x field
  #   > column  is location of y field
  row, column = r, c


  # Check for Out of Bounds
  #   > rowMin is the minimum row value for the bomb search
  #   > If row - 1  is at location zero then don't search behind it
  if(row > 0):
    rowMin = row - 1
  else:
    rowMin = row
  

  #   > columnMin is the minimum column value for the bomb search
  #   > If column - 1 is at location zero then don't search behind it
  if(column > 0):
    columnMin = c - 1
  else:    columnMin = column


  # Check for Out of Bounds
  #   > rowMax is the maximum row value for the bomb search
  #   > If row + 1 is greater than gameboard size, then don't search after it
  if(row + 1 < len(b)):
    rowMax = row + 2
  else:
    rowMax = row + 1


  #   > columnMax is the maximum column value for the bomb search
  #   > If column + 1 is greater than gameboard size, then don't search after it
  if(column + 1 < len(b[0])):
    columnMax = column + 2
  else:
    columnMax = column + 1


  # Bombs near field
  #   > bombCount is the quantity of bombs near the field
  #   > iterates for the selected range
  bombCount = 0
  for sweepX in range (rowMin, rowMax):
    for sweepY in range (columnMin, columnMax):
      bombCount += isBomb(sweepX, sweepY, b)


  # If Field is Bomb
  #   > Subtract one from bombCount
  #   > This test doesn't matter because if the field is a bomb, player loses
  if(isBomb(row, column, b) == 1):
    bombCount -= 1
  
  # Quantity of safe fields
  safeCount = 8 - bombCount


  # return bombCount and safeCount
  return bombCount, safeCount
  

#  ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~  #


# Reveal Near Fields that are Safe
#   > r is location of row
#   > c is location of columns
#   > b is the Minesweeper board
#   > Returns an int
def solveField(r, c, b):
  # Work in Progress
  return 1