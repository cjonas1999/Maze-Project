from enum import Enum

class Square(Enum):
	WALL = 1
	OPEN = 2
	START = 3
	FINISH = 4

class MazeReader:
	def __init__():


	def toString():


	def fromChar(ch):
		if (ch == '#'):
			return Square.WALL
		elif (ch == '.'):
			return Square.OPEN
		elif (ch == 'o'):
			return Square.START
		elif (ch == '*'):
			return Square.FINISH
		else:#invalid argument passed
			raise ValueError