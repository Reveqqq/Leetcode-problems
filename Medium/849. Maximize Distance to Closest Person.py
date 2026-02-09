from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDist, prev = 0, -1
        for i, n in enumerate(seats):
            if n:
                dist = i if prev == -1 else (i - prev) // 2
                maxDist = max(maxDist, dist)
                prev = i
            
        if not seats[i]:
            maxDist = max(maxDist, i - prev)
        
        return maxDist
             


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDistToClosest(seats = [1,0,0,1]))
    print(sol.maxDistToClosest(seats = [1,0]))
    print(sol.maxDistToClosest(seats = [0,1]))
    print(sol.maxDistToClosest(seats = [1,0,0,0,1,0,1]))
    print(sol.maxDistToClosest(seats = [0,0,0,1,1,0,1]))
    print(sol.maxDistToClosest(seats = [1,0,0,1,0,0,0]))
    print(sol.maxDistToClosest(seats = [0,1,0,0,0,0,0,0,1,1,0,1,1]))