from enum import Enum

class Square(Enum):
	WALL = 1
	OPEN = 2
	START = 3
	FINISH = 4
    
class Solution():
	solx = []
	soly = []
    
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
		print(self.rows)
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
		self.visited = []
		for i in range(self.mazereader.rows):
			self.visited.append([])
			for j in range(self.mazereader.cols):
				self.visited[-1].append(False)
        
	def solve(self, x, y):
		Solution.solx.append(x)
		Solution.soly.append(y)
		self.visited[x][y]=True
        
		print(Solution.solx[len(Solution.solx)-1], Solution.soly[len(Solution.solx)-1])
        
		if(self.mazereader.maze[x][y]==Square.FINISH):
			for i in len(Solution.sol):
				self.mazereader.maze[Solution.solx.pop][Solution.soly.pop] = 'x'

		if(self.mazereader.maze[x+1][y]==Square.OPEN and True !=self.visited[x+1][y]):
			self.solve(x+1, y)
		elif(self.mazereader.maze[x][y+1]==Square.OPEN and True !=self.visited[x][y+1]):
			self.solve(x, y+1)
		elif(self.mazereader.maze[x-1][y]==Square.OPEN and True !=self.visited[x-1][y]):
			self.solve(x-1, y)
		elif(self.mazereader.maze[x][y-1]==Square.OPEN and True !=self.visited[x][y-1]):
			self.solve(x, y-1)
    
	def start(self):
		found = 0
		startx = 0
		starty = 0
		while(found==0):
			for i in range(self.mazereader.rows):
				for j in range(self.mazereader.cols):
					if(self.mazereader.maze[i][j] == Square.START):
						found = 1
						startx=i
						starty=j
		if(found == 0 or found > 1):
			raise ValueError('No start point found or Multiple start points found')
		self.solve(startx, starty)
        
maze = MazeReader()
solver = MazeSolver(maze)
solver.start()
