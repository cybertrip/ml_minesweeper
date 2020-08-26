#  Import other Python files  #
"""
	> numpy		necessary for creating two dimensional array
"""
import numpy as np

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
	gameboard = np.full((row, column), 0) 


	#  Station bomb instances  #
	"""
		> Stations bombs at random locations
		> Quantity of bombs determined by difficulty scale
	"""
	gameboard[2][1] = 1


	#  Return gameboard  #
	"""
		> Returns constructed gameboard 
	"""
	return gameboard