# If debug is True, debbuging messages will be logged on execution.
debug = True

prompt_message = """\

Instructions:
    1.Create the maze row by row.
    2.Enter an empty row to quit.
"""

# Display the Instructions.
print(prompt_message)

# Get the input row by row.
rows = []
while True:
    row = input()
    if ".txt" in row:
        maze_file = open(row, encoding="utf-8")
        rows_file = maze_file.read()
        print()
        break
    if row:
        rows.append(row)
    else:
        break

if (debug):
    print("Debugging:")
    if rows:
        display_rows = '\n'.join(rows)
        print(display_rows)
    elif rows_file:
        print(rows_file)
