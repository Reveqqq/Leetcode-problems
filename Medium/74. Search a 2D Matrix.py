from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = m - 1
        while l <= r:
            mid = l + (r - l) // 2
            if  matrix[mid][0] == target:
                return True
            
            elif matrix[mid][0] > target:
                r = mid - 1
            
            else:
                l = mid + 1
        row = r
        
        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2
            if  matrix[row][mid] == target:
                return True
            
            elif matrix[row][mid] > target:
                r = mid - 1
            
            else:
                l = mid + 1

        return False


if __name__ == "__main__":
    sol = Solution()

    print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(sol.searchMatrix(matrix = [[1]], target = 1))
    print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 11))
