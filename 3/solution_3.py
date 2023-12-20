
import math as m
import re


test_engine = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

board = list(open("3\input_3.txt"))
symbols_location = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

print(chars)


# User

'''board = list(open('data.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
         if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p) for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p) == 2))
expliquer'''
