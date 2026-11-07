class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dp = [[0 for c in range(COLS)] for r in range(ROWS)] 

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            if dp[r][c] != 0:
                return 0
            # print(r, c)

            dp[r][c] = 1

            top = dfs(r - 1, c)
            right = dfs(r, c + 1)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)

            cur_area = 1 + top + right + left + down

            return cur_area

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and dp[r][c] == 0:
                    res = max(res, dfs(r, c))


        return res