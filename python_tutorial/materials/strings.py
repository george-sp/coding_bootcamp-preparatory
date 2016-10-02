import string

single_double_quotes = 'Here is how we can include single and double quotes inside a single quoting string:'
print(single_double_quotes)
print('"Isn\'t", she said.')
print()

new_line = ('The character \'\\n\' embeds a newline character in a string.\n'
            'When the print() function encounters \'\\n\' in a string, it will start a new line:')
print(new_line)
print('First line.\nSecond line.')
print()

spanning_multiple_lines = ('End of lines are automatically included in the string,\n'
                           'but it\'s possible to prevent this by adding a \\ at the end of the line.')
print(spanning_multiple_lines)
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print()

string_concatenation = 'Strings can be concatenated (glued together) with the + operator, and repeated with *.'
print(string_concatenation)
# 3 times 'un', followed by 'ium'
s = 3 * 'un' + 'ium'
print(s)
print(3 * 'un' + 'ium')
print()

literal_strings = 'Two or more string literals next to each other are automatically concatenated:'
print("'Py''thon'", "=",'Py''thon')
print()

string_indexing = 'Strings can be indexed:'
print(string_indexing)
word = 'Python'
# Print character in position 0.
print('word[0]', '=', word[0])
# Print character in position 5.
print('word[5]', '=', word[5])
# print the last character.
print('word[-1]', '=', word[-1])
# Print second last character.
print('word[-2]', '=', word[-2])
print('word[-6]', '=', word[-6])
print()

string_slicing = 'In addition to indexing, slicing is also supported:'
print(string_slicing)
# Print characters from position 0 (included) to 2 (excluded).
print('word[0:2]', '=', word[0:2])
# Print characters from position 2 (included) to 5 (excluded).
print('word[2:5]', '=', word[2:5])
# This makes sure that s[:i] + s[i:] is always equals to s.
print('word[:2] + word[2:]', "=", word[:2] + word[2:])
print('word[:4] + word[4:]', "=", word[:4] + word[4:])
# Print character from the beginning to position 2 (excluded).
print('word[:2]', "=", word[:2])
# Print characters from position 4 (included) to the end.
print('word[4:]', "=", word[4:])
# Print characters from the second-last (included) to the end.
print('word[-2:]', "=", word[-2:])
print()

string_immutability = 'Python strings cannot be changed - they are IMMUTABLE'
print(string_immutability)
print('\'J\' + word[1:]', '=', 'J'+ word[1:])
print('word[:2] + \'py\'', '=', word[:2] + 'py')
print()

s = 'supercalifragilisticexpialidocious'
print("The len() of", s, "=", len(s))
print()

string_unicode = 'A string is a sequence of Unicode code points.'
print(string_unicode)
s = 'Hello, World'
print(s)
for x in s:
    print(ord(x), end=":")
print()

string_ascii = 'ASCII is an older character encoding:'
print(string_ascii)
for char in string.ascii_uppercase:
    print(char, "=", ord(char), end=" ")
print()
for char in string.ascii_lowercase:
    print(char, "=", ord(char), end=" ")
print()
print()

print('A numeric string is not a number:')
s = '12345'
print(s)
for x in s:
    print(ord(x), end=":")
print()

print('Convert a number to a character using the chr() function:')
for x in [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100]:
    print(chr(x), end="")
print("\n")

print('A string can be split on a specific character using the split() method:', "\n")
print("'1,2,3'.split(','): ", '1,2,3'.split(','), "\n")
print("'1,2,3'.split(',', maxsplit=1): ", '1,2,3'.split(',', maxsplit=1), "\n")
print("'1,2,,3,'.split(','): ", '1,2,,3,'.split(','), "\n")
print("'1 2  3   4'.split(): ", '1 2  3   4'.split(), "\n")
