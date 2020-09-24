from enum import Enum

class Square(Enum):
	WALL = 1
	OPEN = 2
	START = 3
	FINISH = 4
	
class MazeReader:
	def __init__(self):
		self.maze = []
		self.rows = 0
		self.cols = 0
		filename = input("Enter maze file name: ")

		f = open(filename, "r")

		for line in f:
			row = []
			for ch in line.strip():
				row.append(MazeReader.fromChar(ch))
			self.maze.append(row)
			self.rows += 1
		
		self.cols = len(self.maze[0])

		f.close()

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

	@staticmethod
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

class MazeSolver:
	def __init__(self, mazereader: MazeReader):
		self.mazereader = mazereader
	
	def solve(self):
		#Mark all the vertices as not visited
		visited = [[False for i in range(self.mazereader.cols)] for j in range(self.mazereader.rows)]
		queue = []

		#Find start square
		for i in range(self.mazereader.rows):
			for j in range(self.mazereader.cols):
				if self.mazereader.maze[i][j] == Square.START:
					queue.append([i, j])
					visited[i][j] = True
					break

		while queue:
			s = queue.pop(0)

			for offset in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
				newsquare = [offset[0] + s[0], offset[1] + s[1]]

				if(newsquare[0] < 0 and newsquare[0] >= self.mazereader.rows and newsquare[1] < 0 and newsquare[1] >= self.mazereader.cols):#checking that the square is valid to visit
					continue

				if(not visited[newsquare[0]][newsquare[1]] and self.mazereader.maze[newsquare[0]][newsquare[1]] != Square.WALL):
						if self.mazereader.maze[newsquare[0]][newsquare[1]] == Square.FINISH:
							return True
						else:
							queue.append(newsquare)
							visited[newsquare[0]][newsquare[1]] = True

		return False