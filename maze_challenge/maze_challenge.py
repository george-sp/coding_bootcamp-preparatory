#! /usr/bin/env python3

import copy
import argparse

# Create a parser
parser = argparse.ArgumentParser(prog="Maze Challenge", description='Solve maze challenges using recursion.')
parser.add_argument('-d', '--debug', action='store_true', dest='debug_mode', help='define debug_mode mode')
args = parser.parse_args()

# If debug_mode is True, debbuging messages will be logged on execution.
debug_mode = args.debug_mode
print("debug_mode = ", debug_mode)

"""
Prompt user to create a maze now(row by row input)
or use a pre-created maze stored in a .txt file.
"""
def getMaze():
    prompt_message = """\

    Instructions:
        1.Create the maze row by row.
        2.Enter an empty row to quit.
        3.Enter a txt file.
    """
    # Display the Instructions.
    print(prompt_message)

    rows = []
    while True:
        row = input()
        # Get the input from a txt file.
        if ".txt" in row:
            maze_file = open(row, encoding="utf-8")
            return maze_file.read()
        # Get the input row by row.
        if row:
            rows.append(row)
        else:
            # If user hits enter join all rows and create the maze.
            return '\n'.join(rows)

"""
Seperate each symbol in each row.
Depict the maze as a list of lists.
"""
def shapeMaze(maze, maze_num_rows):
    for r in range (maze_num_rows):
        maze[r] = list(maze[r])
    return maze

"""
Returns the number of rows and
the number of columns of the maze.
"""
def getMazeDimensions(maze):
    return len(maze), len(maze[0])

"""
Returns the coordinates of the maze structure.
"""
def getMazeCoordinates(height, width):
    # Initialize a list of (maze_rows_len) lists of (maze_cols_len) lists.
    maze_coords = [[[] for y in range(width)] for x in range(height)]
    # Iterate through the maze_coords list and set the appropriate coordinates.
    for r in range (height):
        for c in range (width):
            maze_coords[r][c] = [r+1, c+1]
    return maze_coords

"""
Finds and returns the coordinates of the starting and ending maze points.
"""
def getMazeStartEnd(height, width):
    start_point = []
    end_point = []
    for r in range (height):
        for c in range (width):
            if maze[r][c] == 'G':
                end_point = maze_coords[r][c]
            if maze[r][c] == 'S':
                start_point = maze_coords[r][c]
    return start_point, end_point

"""
Finds and returns the coordinates of the block points in a maze.
"""
def getMazeBlocks(height, width):
    block_points = []
    for r in range (height):
        for c in range (width):
            if maze[r][c] == 'X':
                block_points.append(maze_coords[r][c])
    return block_points

"""
Find the best maze solution(s)
"""
def getBestSolutions(maze_solutions):
	best_solutions = []
	solution_steps = []
	min_steps = 0
	for solution in maze_solutions:
		solution_steps.append(solution[-1][-1])

	min_steps = min(solution_steps)
	
	for best_solution_index in [i for i, steps in enumerate(solution_steps) if steps == min_steps]:
		best_solutions.append(maze_solutions[best_solution_index])
	
	return best_solutions

"""
Print maze in terms of X, G, S
"""
def printMaze(maze_columns_length, maze_rows_length, maze_shaped):
	print("  ", end="")
	for i in range (maze_cols_len):
		print(" ", i + 1, " ", end="")
	print()
	for i in range (maze_rows_len):
		print(i + 1, maze[i])

"""
Print the  coordinates of the maze
"""
def printMazeCoordinates(maze_coordinates):
	for row in maze_coordinates:
		print(row)

"""
Print maze solution in terms of X, G, S and numbers for each step-cell
"""
def printMazeSolution(maze_columns_length, maze_rows_length, maze_shaped, maze_solution):
	maze_shaped_solution = copy.deepcopy(maze_shaped)
	
	for solution_step in maze_solution:
		maze_shaped_solution[solution_step[0] - 1][solution_step[1] - 1] = str(solution_step[2])

	printMazeCoordinates(maze_shaped_solution)

"""
A better formatted printMazeSolution
"""
def printFormattedMazeSolution(maze_columns_length, maze_rows_length, maze_shaped, maze_solution):
	maze_shaped_solution = copy.deepcopy(maze_shaped)

	for solution_step in maze_solution:
		maze_shaped_solution[solution_step[0] - 1][solution_step[1] - 1] = str(solution_step[2])

	for row in range (len(maze_shaped_solution)):
		for column in range (len(maze_shaped_solution[row])):
			maze_cell = maze_shaped_solution[row][column]
			if (len(maze_cell) == 1):
				maze_cell = " " + maze_cell + " " if isInt(maze_cell) else 3 * maze_cell
			elif (len(maze_cell) == 2):
				maze_cell = " " + maze_cell
			maze_shaped_solution[row][column] = maze_cell

	s = [[str(e) for e in row] for row in maze_shaped_solution]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print ('\n'.join(table))

"""
Helper method to check if a string represents an int
"""
def isInt(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

"""
Call this method recursively and search for the exit path.
"""
def searchNeighboringCoords(coord, coords_path):
	if (debug_mode): print("Current cell:", coord)
	if (debug_mode): print("Current path:", coords_path)

	# Add the current coord to the path
	cells_path = list(coords_path)
	cells_path.append(coord)

	if (coord[0] == maze_goal[0] and coord[1] == maze_goal[1]):
		if (debug_mode): print("========================================\nSolution Found: %s\n========================================\n" % cells_path)
		list_coords.append(cells_path)

	if (debug_mode): print("Blocks: ", maze_blocks)

    # Create a list of the four adjacent cells
    # with a counter variable of the current element's counter variable +1.
	adjacent_coords = [
	[coord[0] - 1, coord[1]], # top adjacent
	[coord[0], coord[1] - 1], # left adjacent
	[coord[0] + 1, coord[1]], # bottom adjacent
	[coord[0], coord[1] + 1]  # right adjacent
	]

	if (debug_mode): print("Adjacent cells:", adjacent_coords)

    # Use a copy the list so that we can iterate and modify at the same time.
	adjacent_coords_copy = adjacent_coords.copy()
	for cell in adjacent_coords_copy:
        # Check if the cell is out of the border.
		if (cell[0] > maze_rows_len or
			cell[0] <= 0 or 
			cell[1] > maze_cols_len or
			cell[1] <= 0):
			if (debug_mode): print("Remove cell: %s, as Out of Border" % cell)
			adjacent_coords.remove(cell)
        # Check if the cell is a block.
		elif (cell in maze_blocks):
			if (debug_mode): print("Remove cell: %s as in Blocks" % cell)
			adjacent_coords.remove(cell)
		# Check if the cell is already in the current path
		else:
			for cell_in_path in coords_path:
				# Remove the step_counter so we can compare them
				cell_in_path = cell_in_path[:-1]
				if cell_in_path == cell:
					if (debug_mode): print("Remove cell: %s, as Already in Path" % cell)
					adjacent_coords.remove(cell)

	if not adjacent_coords:
		if (debug_mode): print("====================> Not any available adjacent cells\n")
		return None
	else:
		if (debug_mode): print("Adjacent cells available:", adjacent_coords)
		for cell in adjacent_coords:
			cell.append(coord[2] + 1)

			if (debug_mode): print("searchNeighboringCoord(%s, %s\n" % (cell, cells_path))
			searchNeighboringCoords(cell, cells_path)

"""
Run the game
"""

maze = getMaze().split("\n")
maze_rows_len, maze_cols_len = getMazeDimensions(maze)
maze = shapeMaze(maze, maze_rows_len)
maze_coords = getMazeCoordinates(height=maze_rows_len, width=maze_cols_len)
maze_start, maze_goal = getMazeStartEnd(height=maze_rows_len, width=maze_cols_len)
maze_blocks = getMazeBlocks(height=maze_rows_len, width=maze_cols_len)

if (debug_mode):
    print("--------------------------\n\tDebugging\n--------------------------")
    print("Number of rows:", maze_rows_len)
    print("Number of columns:", maze_cols_len)
    print("Start:", maze_start)
    print("Goal:", maze_goal)
    print("Blocks:", maze_blocks)

    print("The Maze:")
    printMaze(maze_cols_len, maze_rows_len, maze)

    print("The Maze Coordinates:")
    printMazeCoordinates(maze_coords)


step_counter = 0
maze_start.append(step_counter)
list_coords = []
searchNeighboringCoords(maze_start, [])


if (debug_mode):
    print("List of coordinates:")
    for list_num in range (len(list_coords)):
    	print("\nSolution %d: %s\nSolution %d:" % (list_num, list_coords[list_num], list_num))
    	printFormattedMazeSolution(maze_cols_len, maze_rows_len, maze, list_coords[list_num])

print("\nTotal solutions found: %d" % len(list_coords))
print("Best Solutions\n--------------")
for i, best_solution in enumerate(getBestSolutions(list_coords)):
	print("\nSolution ", i, ":")
	printFormattedMazeSolution(maze_cols_len, maze_rows_len, maze, best_solution)
