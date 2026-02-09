from typing import List

class Solution:
    #1. set l to first empty seat, r = l
    #2. find first r closet seat
    #3. calc maxDist
        # if l == 0, maxDist = r
        # elif r == len(seats) - 1, maxDist = r - l + 1 # maybe this one after loop
        # else maxDist = (r - l) // 2 + 1
    #4. repaet 1-3 while l != len(seats) and r < len

    def maxDistToClosest(self, seats: List[int]) -> int:
        def firstEmptySeat(l,seats):
            while l < len(seats) and seats[l] == 1:
                l += 1
            return l

        r = l = firstEmptySeat(0, seats)
        maxDist = 1
        N = len(seats)

        while l < N:
            while r < N and seats[r] == 0:
                r += 1
            
            if l == 0:
                maxDist = max(maxDist,r)
            elif r == N and seats[r - 1] == 0:
                maxDist = max(maxDist, r - l)
            else:
                c = (r - l)
                if c % 2 == 0:
                    maxDist = max(maxDist, c // 2)
                else:    
                    maxDist = max(maxDist, c // 2 + 1)

            r = l = firstEmptySeat(r, seats)

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