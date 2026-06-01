class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square_board = {}
        row_board = {}
        column_board = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                key = (i//3, j//3)
                if key not in square_board:
                    square_board[key] = set()
                if i not in row_board:
                    row_board[i] = set()
                if j not in column_board:
                    column_board[j] = set()

                if board[i][j] in square_board[key]:
                    return False
                if board[i][j] in row_board[i]:
                    return False
                if board[i][j] in column_board[j]:
                    return False

                square_board[key].add(board[i][j])
                row_board[i].add(board[i][j])
                column_board[j].add(board[i][j])
                
        return True