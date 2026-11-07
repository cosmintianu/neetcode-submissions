class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_color = image[sr][sc]

        if color == curr_color:
            return image

        ROWS, COLS = len(image), len(image[0])


        def bfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != curr_color:
                return

            image[r][c] = color

            bfs(r + 1,c)
            bfs(r,c + 1)
            bfs(r - 1,c)
            bfs(r,c - 1)

        bfs(sr, sc)
        return image
