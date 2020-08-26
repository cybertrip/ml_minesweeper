#  Main Driver  #
"""
	> Main driver for executing whole program
	> Just for tidiness of code
"""

#  Import other Python files  #
"""
	> gameboard		layout for Minesweeper gameboard
"""
from minesweeper import *

print("Create gameboard")
gameboard = gameboard(9, 9, 2)

print(gameboard)
