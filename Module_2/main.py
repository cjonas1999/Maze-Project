import maze

def main():
	mr = maze.MazeReader()
	ms = maze.MazeSolver(mr)
	print(ms.solveBFS())

main()