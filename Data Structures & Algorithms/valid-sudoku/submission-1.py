class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking the rows:
        for row in range(9):
            no_spaces = [board[row][col] for col in range(9) if board[row][col].isdigit()]
            no_dup = set(no_spaces)

            if len(no_spaces) != len(no_dup):
                return False

        # checking the cols:
        for col in range(9):
            no_spaces = [board[row][col] for row in range(9) if board[row][col].isdigit()]
            no_dup = set(no_spaces)

            if len(no_spaces) != len(no_dup):
                return False

        # Checking 3 x 3 squares
        for n in range(9):
            start_row = (n // 3) * 3
            start_col = (n % 3) * 3
            
            no_spaces = []
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col+ 3):
                    if board[row][col].isdigit():
                        no_spaces.append(board[row][col])

            no_dup = set(no_spaces)

            if len(no_spaces) != len(no_dup):
                return False

        return True
            
