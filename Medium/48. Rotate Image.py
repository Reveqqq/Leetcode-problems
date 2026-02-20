from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 90 = transpose + reverse row
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

        # 180 = reverse row + reverse column
        # matrix.reverse()
        # for row in matrix:
        #     row.reverse()

        # 270 = transpose + reverse col
        # for i in range(n):
        #     for j in range(i,n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # matrix.reverse()


        

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(matrix)
    print(matrix)
