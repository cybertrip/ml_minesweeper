#  Minesweeper  #
"""
	> Sets rule of Minesweeper game
	> Creates gameboard
	> Both human and machine will interact with rules
"""


#  Import other Python files  #
"""
	> numpy		necessary for creating two dimensional array
	> random	generating random numbers for element selection
"""
import numpy as gb
import random


#  Create Minesweeper gameboard  #
"""
	> r is quantity of row
	> c is quantity of columns
	> d is scale of difficulty
	> Returns the gameboard
"""
def layoutBoard(r, c, d):
	#  Dimensions of gameboard  #
	"""
		> row 		is size of gameboard's width
		> column 	is size of gameboard's length
	"""
	row, column = r, c


	#  Difficulty of gameboard  #
	"""
		> Difficulty will be a scale based number
		> Scale theoretical maximum is determined by gameboard dimensions
		> Scale will be between 0 and 9 (a ten point system)
	"""
	difficulty = d


	#  Initialize gameboard  #
	"""
		> gameboard is a two dimensional array
		> all indices that are safe are initialized as 0
	"""
	#gameboard = [[0] * column] * row
	gameboard = gb.full((row, column), 0) 


	#  Station bomb instances  #
	"""
		> Stations bombs at random locations
		> fields is the quantity of each element of gameboard
		> bombScale is the quantity of bombs in ratio to gameboard size
		> bombQuantity is the quantity of bombs in the gameboard
		> bombCount is the incrementer for the while loop
		> while loop will run until each unique field is a bomb
		> 1 is bomb, 0 is safe
	"""
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
	
	
	#  Return gameboard  #
	"""
		> Returns constructed gameboard 
	"""
	return gameboard


#  ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~  #


#  Is the field a bomb  #
"""
	> r is location of row
	> c is location of columns
	> Returns a boolean
"""
def isBomb(r, c, gameboard):
	#  Location of field  #
	"""
		> row 		is location of x field
		> column 	is location of y field
	"""
	row, column = r, c


	#  Check if bomb  #
	"""
		> If bomb return 1
		> If safe return 0
	"""
	if gameboard[row][column] != 0:
		return 1
	else:
		return 0


#  ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~  #


#  Quantity of bombs surrounding field  #
"""
	> r is location of row
	> c is location of columns
	> Returns an int
"""
def nearBomb(r, c, gameboard):
	#  Location of field  #
	"""
		> row 		is location of x field
		> column 	is location of y field
	"""
	row, column = r, c


	#  Bombs near field  #
	"""
		> 
	"""
	bombCount = 0
	for sweepX in range (-1, 2):
		for sweepY in range (-1, 2):
			bombCount += isBomb(row + sweepX, column + sweepY, gameboard)
	
	return bombCount
	

#  ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~  #


#  Quantity of bombs surrounding field  #
"""
	> r is location of row
	> c is location of columns
	> Returns an int
"""