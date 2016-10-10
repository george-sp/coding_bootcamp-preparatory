# If debug is True, debbuging messages will be logged on execution.
debug = True

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


maze = getMaze().split("\n")
maze_rows_len, maze_cols_len = getMazeDimensions(maze)
maze = shapeMaze(maze, maze_rows_len)
maze_coords = getMazeCoordinates(height=maze_rows_len, width=maze_cols_len)
maze_start, maze_goal = getMazeStartEnd(height=maze_rows_len, width=maze_cols_len)
maze_blocks = getMazeBlocks(height=maze_rows_len, width=maze_cols_len)

# List of coordinates which will be used as a queue.
# The queue will be initialized with one coordinate, the end coordinate.
# Each coordinate will also have a counter variable attached.
step_counter = 0
maze_goal.append(step_counter)
list_coords = [maze_goal]
# Go through every element in the queue.
for coord in list_coords:
    # Create a list of the four adjacent cells
    # with a counter variable of the current element's counter variable +1.
    adjacent_coords = [
    [coord[0] - 1, coord[1], step_counter], # top adjacent
    [coord[0], coord[1] - 1, step_counter], # left adjacent
    [coord[0] + 1, coord[1], step_counter], # bottom adjacent
    [coord[0], coord[1] + 1, step_counter]  # right adjacent
    ]

    if (debug):
        print(adjacent_coords)


if (debug):
    print("  Debugging  \n-------------")
    print("Number of rows:", maze_rows_len)
    print("Number of columns:", maze_cols_len)
    print("Start:", maze_start)
    print("Goal:", maze_goal)
    print("Blocks:", maze_blocks)
    print("The Maze:")
    print("  ", end="")
    for i in range (maze_cols_len):
        print(" ", i + 1, " ", end="")
    print()
    for i in range (maze_rows_len):
        print(i + 1, maze[i])
    print("The Maze Coordinates:")
    for row in maze_coords:
        print(row)
    print("List of coordinates:")
    print(list_coords)