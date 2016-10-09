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
    if row:
        rows.append(row)
    else:
        break

if (debug):
    print("Debugging:")
    display_rows = '\n'.join(rows)
    print(display_rows)
