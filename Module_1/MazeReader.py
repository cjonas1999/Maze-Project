from enum import Enum

class Square(Enum):
	WALL = 1
	OPEN = 2
	START = 3
	FINISH = 4
    
class MazeReader:
	def __init__():
        
        
	def toString(array):
		az = []
		for i in range(r):
			az.append([])
			for j in range(c):
				az[-1].append("")

		for i in range(r):	
			for j in range(c):
				if (array[i][j]==Square.WALL):
					az[i][j] = '#'
				elif (array[i][j]==Square.OPEN):
					az[i][j] = '.'
				elif (array[i][j]==Square.START):
					az[i][j] = 'o'
				elif (array[i][j]==Square.FINISH):
					az[i][j] = '*'
				else:
					raise ValueError
		return az
        
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