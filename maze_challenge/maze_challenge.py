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

def shapeMaze(maze, maze_num_rows):
    for r in range (maze_num_rows):
        maze[r] = list(maze[r])
    return maze

maze = getMaze().split("\n")
maze_rows_len = len(maze)
maze = shapeMaze(maze, maze_rows_len)

if (debug):
    print("  Debugging  \n-------------")
    print("Number of rows:", maze_rows_len)
    for row in maze:
        print(row)
