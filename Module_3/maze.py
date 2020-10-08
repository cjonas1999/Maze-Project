from enum import Enum
from tkinter import *
import tkinter.simpledialog

class Square(Enum):
	WALL = 1
	OPEN = 2
	START = 3
	FINISH = 4
	
class MazeReader:
	def __init__(self, filename, window, canvas):
		self.maze = []
		self.graphicsMaze = []
		self.rows = 0
		self.cols = 0

		f = open(filename, "r")

		for line in f:
			row = []
			for ch in line.strip():
				item = MazeReader.fromChar(ch)
				row.append(item)
				
			self.maze.append(row)
			self.rows += 1
		
		self.cols = len(self.maze[0])
		
		xscale = 20
		yscale = 20
		for i in range(self.rows):
			graphicsRow = []
			for j in range(self.cols):
				if (self.maze[i][j] == Square.WALL):
					graphicsRow.append(canvas.create_rectangle(j*xscale, i*yscale, (j+1)*xscale, (i+1)*yscale, fill="black"))
				elif (self.maze[i][j] == Square.OPEN):
					graphicsRow.append(canvas.create_rectangle(j*xscale, i*yscale, (j+1)*xscale, (i+1)*yscale, fill="white"))
				elif (self.maze[i][j] == Square.START):
					graphicsRow.append(canvas.create_rectangle(j*xscale, i*yscale, (j+1)*xscale, (i+1)*yscale, fill="red"))
				elif (self.maze[i][j] == Square.FINISH):
					graphicsRow.append(canvas.create_rectangle(j*xscale, i*yscale, (j+1)*xscale, (i+1)*yscale, fill="blue"))
			
			self.graphicsMaze.append(graphicsRow)


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
	
	def solve(self, window, canvas, stepButton, autoButton):
		#Mark all the vertices as not visited
		self.visited = [[False for i in range(self.mazereader.cols)] for j in range(self.mazereader.rows)]
		self.previous = [[[None, None] for i in range(self.mazereader.cols)] for j in range(self.mazereader.rows)]
		self.path = []
		self.queue = []
		self.found = False

		#Find start square
		for i in range(self.mazereader.rows):
			for j in range(self.mazereader.cols):
				if self.mazereader.maze[i][j] == Square.START:
					self.queue.append([i, j])
					self.visited[i][j] = True
					break


		#Create step and auto buttons
		step = IntVar()
		step.set(0)

		stepButton.configure(command=lambda:step.set(step.get()+1))
		autoButton.configure(command=lambda: step.set(-1))

		while not self.found:
			if step.get() < 0:
				window.after(500, self.solveStep(canvas))
			else:
				window.wait_variable(step)
				self.solveStep(canvas)

		

	def solveStep(self, canvas):
		if self.queue and not self.found:
			s = self.queue.pop(0)

			for offset in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
				newsquare = [offset[0] + s[0], offset[1] + s[1]]

				if(newsquare[0] < 0 and newsquare[0] >= self.mazereader.rows and newsquare[1] < 0 and newsquare[1] >= self.mazereader.cols):#checking that the square is valid to visit
					continue

				if(not self.visited[newsquare[0]][newsquare[1]] and self.mazereader.maze[newsquare[0]][newsquare[1]] != Square.WALL):
						self.queue.append(newsquare)
						self.visited[newsquare[0]][newsquare[1]] = True
						self.previous[newsquare[0]][newsquare[1]] = s
						canvas.itemconfig(self.mazereader.graphicsMaze[newsquare[0]][newsquare[1]], fill='grey')

						if self.mazereader.maze[newsquare[0]][newsquare[1]] == Square.FINISH:#calculate path
							curr = newsquare
							while self.mazereader.maze[curr[0]][curr[1]] != Square.START:
								self.path.insert(0, curr)
								canvas.itemconfig(self.mazereader.graphicsMaze[curr[0]][curr[1]], fill='green')
								curr = self.previous[curr[0]][curr[1]]
							self.path.insert(0, curr)#insert start position into path
							self.found = True
		else:
			self.found = True



class MazeApp():
	def __init__(self):
		self.window = Tk()
		self.canvas = Canvas(self.window, height=500, width=500)

		self.loadButton = Button(self.window, text="Load", command=self.loadButtonFunc)
		self.loadButton.pack()

		self.solveButton = Button(self.window, text="Solve", state=DISABLED, command=self.solveButtonFunc)
		self.solveButton.pack()

		
		self.stepButton = Button(self.window, text="Step", state=DISABLED)
		self.stepButton.pack()

		self.autoButton = Button(self.window, text="Auto", state=DISABLED)
		self.autoButton.pack()

		self.window.mainloop()
	
	def loadButtonFunc(self):
		filename = tkinter.simpledialog.askstring(title="Test", prompt="Enter filename:")
		self.canvas.delete("all")
		self.mr = MazeReader(filename, self.window, self.canvas)
		self.canvas.pack()
		self.solveButton.config(state = NORMAL)

	def solveButtonFunc(self):
		self.ms = MazeSolver(self.mr)
		self.stepButton.config(state = NORMAL)
		self.autoButton.config(state = NORMAL)
		self.ms.solve(self.window, self.canvas, self.stepButton, self.autoButton)
