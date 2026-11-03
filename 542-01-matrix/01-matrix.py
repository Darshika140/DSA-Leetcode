
from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

        rows = len(mat)
        columns = len(mat[0])

        queue = deque()

        # Distance matrix
        distance = [[-1] * columns for _ in range(rows)]

        # Add all zeroes to queue
        for row in range(rows):
            for column in range(columns):

                if mat[row][column] == 0:
                    queue.append((row, column))
                    distance[row][column] = 0

        # Directions
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        # BFS
        while queue:

            current_row, current_column = queue.popleft()

            for row_change, column_change in directions:

                neighbour_row = current_row + row_change
                neighbour_column = current_column + column_change

                # Check boundaries and whether visited
                if (0 <= neighbour_row < rows and
                    0 <= neighbour_column < columns and
                    distance[neighbour_row][neighbour_column] == -1):

                    distance[neighbour_row][neighbour_column] = (
                        distance[current_row][current_column] + 1
                    )

                    # IMPORTANT: Append only inside IF
                    queue.append((neighbour_row, neighbour_column))

        return distance
