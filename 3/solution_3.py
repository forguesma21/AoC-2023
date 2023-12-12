
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

board = list(test_engine)
print(board)

board = list(open('input_3.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
         if board[r][c] not in '01234566789.'}
