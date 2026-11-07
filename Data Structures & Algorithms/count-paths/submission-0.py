class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n

        dp = [[-1] * COLS for _ in range(ROWS)]
        print(dp)

        def dfs(r, c):
            if r>=ROWS or c>= COLS:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            if r==ROWS-1 and c==COLS-1:
                return 1

            right = dfs(r, c + 1)
            down = dfs(r + 1, c)

            return right + down


        return dfs(0,0)
