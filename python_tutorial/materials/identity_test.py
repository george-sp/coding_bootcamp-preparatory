"""
Identity testing
- The keyword "is" is used for identity testing.
- The negation is "not is".
- Identity testing means checking that two objects are the same, not that they are equal.
- A frequent use of is is against None: x is None, x is not None, not x is None.
"""

a = "a"
b = "b"
c = a + b
d = "ab"

print('a = "a"\nb = "b"\nc = a + b\nd = "ab"\n')
print("c == d:", c == d)
print ("c is d:", c is d)

print("==================\n")

rb = range(10)
ra = range(10)

print("rb = range(10)\nra = range(10)\n")
print("ra == rb:", ra == rb)
print("ra is rb:", ra is rb)
