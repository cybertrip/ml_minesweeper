#  Import other Python files  #
"""
	> numpy		necessary for creating two dimensional array
"""
import numpy as gb
import random

def gameboard(r, c, d):
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