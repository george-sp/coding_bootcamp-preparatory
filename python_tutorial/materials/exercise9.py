"""
This is a program that asks for the number of positions to shift each character
and a phrase.
Then it will output the phrase encrypted with the Caesar cipher.
The Caesar cipher works by substituting each character in a message with a
character that occurs x places later on the alphabet,
wrapping around from the beginning, if needed.

* Assume that the phrase consists only of uppercase English letters
  (without punctuation or spaces).
"""

ALPHABET_SIZE = 26

# Ask for the number of positions to shift and the phrase to be encrypted.
shift = int(input("Enter shift: "))
phrase = input("Enter phrase: ")

# Initialize the cipher text.
cipher = ""

# If the shift number is bigger than the alphabet, adjust it.
if (shift >= ALPHABET_SIZE):
    shift = shift % ALPHABET_SIZE
    print(shift)

# Iterate through the given phrase.
for c in phrase:
    # Find the new character.
    new_char = ord(c) + shift
    # Check if the numerical representation of the new character in ASCII
    # is bigger than the last character of the alphabet.
    if (new_char > ord('Z')):
        cipher += chr(ord('A') - 1 + (new_char - ord('Z')))
        continue
    cipher += chr(new_char)

# Print the encrypted text.
print(cipher)
