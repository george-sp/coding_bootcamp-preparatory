# Coding Bootcamp: Maze Challenge

Search in a maze and find all possible solutions

------------------------------------------------------------------------

### How-tos


#### Create a maze

**Symbols**
- `X` -- A blocked cell
- `_` -- A free cell
- `S` -- The starting cell
- `G` -- The goal cell

**Sample**
```
X___X
S_X_G
X_XX_
X____
```

#### Run maze_challenge.py

**Usage**
`./maze_challenge.py -h`
```
usage: maze_challenge.py [-h] [-d] [maze_input_file]

Solve maze challenges using recursion.

positional arguments:
  maze_input_file  specify a txt file with a maze

optional arguments:
  -h, --help       show this help message and exit
  -d, --debug      define debug_mode mode

Have fun!
```

**Solve the Sample**
`./maze_challenge.py sample.txt`
```
Total solutions found: 2
Best Solutions
--------------

Solution  0 :
XXX	 2 	 3 	 4 	XXX
 0 	 1 	XXX	 5 	 6 
XXX	___	XXX	XXX	___
XXX	___	___	___	___

```

**See all Solutions**
`./maze_challenge.py --debug sample.txt`
