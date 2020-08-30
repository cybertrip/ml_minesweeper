#  Main Driver
#		> Main driver for executing whole program
#		> Just for tidiness of code

#	Import other Python files
#		> gameboard		layout for Minesweeper gameboard
#		> interface		human / machine control of Minesweeper game
from minesweeper import *
from interface	 import *

print("Create gameboard")
gameboard = layoutBoard(9, 9, 5)

print(gameboard)
print(nearBomb(4, 4, gameboard))