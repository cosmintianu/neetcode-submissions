class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        col_set = [set() for _ in range(ROWS)]
        square_set = [set() for _ in range(9)]
        for row in range(ROWS):
            row_set = set()

            for col in range(COLS):
                square_idx = 3 * (row // 3) + col // 3
                if board[row][col] != '.' and board[row][col] in square_set[square_idx]:
                    # print(square_idx, row, col)
                    return False

                square_set[square_idx].add(board[row][col])


                if board[row][col] != '.' and board[row][col] in col_set[col]:
                    # print(row, col)
                    return False

                col_set[col].add(board[row][col])


                if board[row][col] != '.' and board[row][col] in row_set:
                    # print(row, col, board[row][col])
                    return False

                row_set.add(board[row][col])

        print(col_set)

        return True