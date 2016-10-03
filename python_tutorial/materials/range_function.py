"""
The range() Function
- If you do need to iterate over a sequence of numbers,
  the built-in function range() comes in handy.
- It generates arithmetic progressions.
- The given end point is never part of the generated sequence
- range(10) generates 10 values, the legal indices for items of a sequence of length 10.
- It is possible to let the range start at another number, or to specify a
  different increment (even negative; sometimes this is called the ‘step’).
- To iterate over the indices of a sequence, you can combine
  range() and len().
- However, it is often more convenient to use the enumerate() function.
- A strange thing happens if you just print a range.
- range() returns something that behaves as if it is a list, but in fact it isn’t.
- It is an object which returns the successive items of the desired sequence
  when you iterate over it, but it doesn’t really make the list, thus saving space.
- We say such an object is iterable, that is, suitable as a target for functions
  and constructs that expect something from which they can obtain successive items
  until the supply is exhausted.
- We have seen that the for statement is such an iterator.
  The function list() is another; it creates lists from iterables.
"""

print("""\
for i in range(5):
    print(i)
""")
for i in range(5):
    print(i)

print("\n------------------------------------------------------------\n")

print("""\
for i in range(5, 10):
    print(i, end=' ')

print()
for i in range(0, 10, 3):
    print(i, end=' ')

print()
for i in range(-10, -100, -30):
    print(i, end=' ')

print()
for i in range(10, -1, -1):
    print(i, end=' ')
""")
for i in range(5, 10):
    print(i, end=' ')

print()
for i in range(0, 10, 3):
    print(i, end=' ')

print()
for i in range(-10, -100, -30):
    print(i, end=' ')

print()
for i in range(10, -1, -1):
    print(i, end=' ')
print()

print("\n------------------------------------------------------------\n")

print("""\
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
""")
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print("\n------------------------------------------------------------\n")

print("""\
for i, j in enumerate(a):
    print(i, j)
""")
for i, j in enumerate(a):
    print(i, j)

print("\n------------------------------------------------------------\n")

print("print(range(10))\n")
print(range(10))

print("\n------------------------------------------------------------\n")

print("list(range(5))\n")
print(list(range(5)))

print("\n------------------------------------------------------------\n")
