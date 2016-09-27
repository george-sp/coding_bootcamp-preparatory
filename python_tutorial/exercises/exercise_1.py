# Write a program that produces the following output:
# 
# 000000001
# 000000022
# 000000333
# 000004444
# 000055555
# 000666666
# 007777777
# 088888888
# 999999999

# Iterate through each line.
for num in range (1, 10):
    # Iterate from the beginning and place 0s.
    for i in range (9 - num):
        print(0, end="")
    # Iterate from the last 0 to the end of the line.
    for i in range (num):
        print(num, end="")
    # Change line.
    if (num < 9):
        print("")
