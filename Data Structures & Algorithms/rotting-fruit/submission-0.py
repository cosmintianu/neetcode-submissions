class Solution:

    from collections import deque

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        fresh = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dir in dirs:
                    nr, nc = r + dir[0], c + dir[1]

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))


        return -1 if fresh > 0 else minutes

        
            

