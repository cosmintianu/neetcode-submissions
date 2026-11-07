class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix) - 1

        for i in range((N + 1)//2):
            matrix[i], matrix[N - i] = matrix[N - i], matrix[i]

        for i in range(0, N + 1):
            for j in range(i + 1, N + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
