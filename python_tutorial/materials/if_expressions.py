"""
if expressions
- Apart from if statements, we also have if expressions.
- These evaluate an expression depending on a condition.
"""

# use the datetime library
import datetime

now = datetime.datetime.now().time()

message = "good morning" if now < datetime.time(12) else "good evening"
print(message)
