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
def getMazeCoordinates():
    # Initialize a list of (maze_rows_len) lists of (maze_cols_len) lists.
    maze_coords = [[[] for y in range(maze_cols_len)] for x in range(maze_rows_len)]
    # Iterate through the maze_coords list and set the appropriate coordinates.
    for r in range (maze_rows_len):
        for c in range (maze_cols_len):
            # The third element is a counter variable.
            # So, it is assigned to 0 during the initialization.
            maze_coords[r][c] = [r+1, c+1, 0]
    return maze_coords

maze = getMaze().split("\n")
maze_rows_len, maze_cols_len = getMazeDimensions(maze)
maze = shapeMaze(maze, maze_rows_len)
maze_coords = getMazeCoordinates()

if (debug):
    print("  Debugging  \n-------------")
    print("Number of rows:", maze_rows_len)
    print("Number of columns:", maze_cols_len)
    print("The Maze:")
    for row in maze:
        print(row)
    print("The Coordinates:")
    for row in maze_coords:
        print(row)
