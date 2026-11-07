class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ROWS, COLS = 9, 9
        squares = {}
        rows = {}
        cols = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                sq_id = (r//3) * 3 + c//3

                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if sq_id not in squares:
                    squares[sq_id] = set() 
                
                if board[r][c] in rows[r] or \
                    board[r][c] in cols[c] or \
                    board[r][c] in squares[sq_id]:
                    return False

                squares[sq_id].add(board[r][c])
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])

        return True
