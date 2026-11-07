class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0
        def bfs(r, c):
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            if r < ROWS - 1:
                bfs(r + 1, c)

            if r > 0:
                bfs(r-1, c)


            if c < COLS-1:
                bfs(r, c + 1)
            
            if c >0:
                bfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r,c)
                    res +=1

        

        return res
