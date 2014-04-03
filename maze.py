import random


maze_matrix = []
#DIRECTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']
DIRECTIONS = [(0,1), (0,-1), (-1,0), (1,0)]

def initialize(size):
	i = 0
	while i < size:
		row = [0] * size
		maze_matrix.append(row)
		i += 1

def generate_maze(size):
	x = 0
	y = 0
	while x + 1 < size and y + 1 < size:
		error = False
		(dx, dy) = DIRECTIONS[random.randint(0,3)]
		if dx:
			if x + dx >= 0:
				x += dx
			else:
				continue
		elif dy:
			if y + dy >= 0:
				y += dy
			else:
				continue

		maze_matrix[x][y] = 1


if __name__ == '__main__':
	size = 20
	initialize(size)
	generate_maze(size)
	for r in maze_matrix:
		print r
