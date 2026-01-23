from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        pair = intervals[0]
        i = 1

        while i < len(intervals):
            next_pair = intervals[i]

            if pair[1] >= next_pair[0]:
                pair[1] = max(pair[1], next_pair[1])
            else:
                ans.append(pair)
                pair = next_pair
            
            i += 1

        ans.append(pair)

        return ans
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge(intervals = []))
    print(sol.merge(intervals = [[1,4], [2,3]]))
    print(sol.merge(intervals = [[2,3], [1,4]]))
    print(sol.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
    print(sol.merge(intervals = [[1,3],[2,6],[5,10],[15,18]]))
    print(sol.merge(intervals = [[1,4],[4,5]]))
    print(sol.merge(intervals = [[4,7],[1,4]]))
