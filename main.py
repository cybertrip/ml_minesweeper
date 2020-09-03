#  Main Driver
#		> Main driver for executing whole program
#		> Just for tidiness of code

#	Import other Python files
#		> gameboard		layout for Minesweeper gameboard
#		> interface		human / machine control of Minesweeper game
from minesweeper import *
from interface	 import *

print("Create gameboard")
gameboard = layoutBoard(9, 9, 3)

print(gameboard)
for x in range (0,9,1):
  print(nearField(x, x, gameboard))