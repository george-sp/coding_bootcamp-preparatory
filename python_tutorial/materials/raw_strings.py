raw_instructions_1 = ("Apart from newlines, \n"
                      "there are other special characters prefaced by \;\n"
                      "for example, \\t is a tab character.")
raw_instructions_2 = ("If you don't characters prefaced by \\ to be interpreted as special characters,\n"
                      "you can use raw strings by adding an r before the first quote.")

print(raw_instructions_1)
print("\t Hello, world!")
print()

print(raw_instructions_2)
# Here \n means newline!
print('C:\some\name')
# Note the r before the quote
print(r'C:\some\name')
print()
