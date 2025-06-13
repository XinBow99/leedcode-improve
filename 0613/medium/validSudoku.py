import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Checks whether the given 9x9 Sudoku board is valid.

        Each row, column, and 3x3 sub-grid must contain the digits 1-9
        with no duplicates. Empty cells are represented by '.'.

        Args:
            board: A 9x9 2D list of strings representing the Sudoku board.

        Returns:
            True if the board is valid according to Sudoku rules, else False.
        """
        # row[r]: digits seen in row r
        # col[c]: digits seen in column c
        # grid[(r//3, c//3)]: digits seen in 3x3 box
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        # Iterate over each cell in the board
        for r in range(9):
            for c in range(9):
                cur_value = board[r][c]

                # Skip empty cells
                if cur_value == ".":
                    continue

                # Check if current value violates Sudoku constraints
                if (
                    cur_value in row[r]  # already seen in same row
                    or cur_value in col[c]  # already seen in same column
                    or cur_value in grid[(r // 3, c // 3)]  # seen in 3x3 grid
                ):
                    return False

                # Record the digit in respective sets
                row[r].add(cur_value)
                col[c].add(cur_value)
                grid[(r // 3, c // 3)].add(cur_value)

        return True
