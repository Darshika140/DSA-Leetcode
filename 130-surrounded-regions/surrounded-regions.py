
from collections import deque

class Solution:
    def solve(self, board):

        rows = len(board)
        columns = len(board[0])

        queue = deque()

        # Four possible directions
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        # Step 1: Find boundary O cells
        for row in range(rows):
            for column in range(columns):

                if (row == 0 or row == rows - 1 or
                    column == 0 or column == columns - 1):

                    if board[row][column] == "O":

                        board[row][column] = "S"
                        queue.append((row, column))

        # Step 2: BFS to find connected safe O cells
        while queue:

            current_row, current_column = queue.popleft()

            for row_change, column_change in directions:

                neighbour_row = current_row + row_change
                neighbour_column = current_column + column_change

                if (0 <= neighbour_row < rows and
                    0 <= neighbour_column < columns and
                    board[neighbour_row][neighbour_column] == "O"):

                    board[neighbour_row][neighbour_column] = "S"

                    queue.append((neighbour_row, neighbour_column))

        # Step 3: Convert surrounded O to X
        # Convert safe S back to O
        for row in range(rows):
            for column in range(columns):

                if board[row][column] == "O":
                    board[row][column] = "X"

                elif board[row][column] == "S":
                    board[row][column] = "O"
