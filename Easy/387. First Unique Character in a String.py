from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:


        hash_map = Counter(s)

        for char in s:
            if char in hash_map and hash_map[char] == 1:
                return s.find(char)

        return -1
        
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar(s='leetcode'))
    print(sol.firstUniqChar(s='loveleetcode'))
    print(sol.firstUniqChar(s='aabb'))
    print(sol.firstUniqChar(s=''))
    print(sol.firstUniqChar(s='b'))


