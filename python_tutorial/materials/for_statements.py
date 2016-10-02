"""
for Statements
- The for statement in Python differs a bit from what you may be used to in C or Pascal.
- It does not always iterate over an arithmetic progression of numbers (like in Pascal).
- It does not give the user the ability to define both the iteration step and halting condition (as C).
- Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

- Do not modify a sequence when you are iterating over it.
- If you do need to do that, do that on a copy of the sequence.
- The slice notation makes this especially convenient.

- Note that if we were appending instead of inserting, then if we were not using a copy we would end up with a disaster.
- We would enter an infinite loop.
- The following code will never end.
"""

words = ['cat', 'window', 'defenestrate']
print("\nDefine a list:")
print("""\
words = ['cat', 'window', 'defenestrate']
""")

# Measure some strings:
print("Measure some strings:", words, "using: words:")
print("""\
    for w in words[:]:  # Loop over a slice copy of the entire list.
        if len(w) > 6:
            words.append(w)
    print(words)
""")
for w in words:
    print(w, len(w))

# Loop over a slice copy of the entire list.
print("\nLoop over a slice copy of the entire list", "using: words[:]")
print("""\
    for w in words[:]:  # Loop over a slice copy of the entire list.
        if len(w) > 6:
            words.append(w)
    print(words)
""")
for w in words[:]:
    if len(w) > 6:
        words.append(w)
print(words)

# If run it press Ctr+C to cancel
print("\nThe following code never ends:")
print("""\
    # Loop over the actual list.
    for w in words:
        if len(w) > 6:
            words.append(w)
    print(words)
""")
