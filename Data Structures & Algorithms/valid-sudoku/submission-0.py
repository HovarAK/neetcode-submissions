class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check if all rows have no duplicates
        for row in range(9):
            duplicates = [val for val in board[row] if val != "."]
            no_duplicates = set(duplicates)

            if len(duplicates) != len(no_duplicates):
                return False
        
        # check if all columns have no duplicates
        for col in range(9):
            duplicates = [board[row][col] for row in range(9) if board[row][col] != "."]
            no_duplicates = set(duplicates)

            if len(duplicates) != len(no_duplicates):
                return False

        # check each 3x3 box
        for i in range(9):
            row_start = (i // 3) * 3
            col_start = (i % 3) * 3

            duplicates = []

            for row in range(row_start, row_start + 3):
                for col in range(col_start, col_start + 3):
                    if board[row][col] != ".":
                        duplicates.append(board[row][col])

            no_duplicates = set(duplicates)

            if len(duplicates) != len(no_duplicates):
                return False

        return True