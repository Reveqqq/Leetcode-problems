from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}

    
        for i in range(len(s)):
            if s[i] not in hash_map_s:
                hash_map_s[s[i]] = i

            if t[i] not in hash_map_t:
                hash_map_t[t[i]] = i

            if hash_map_s[s[i]] != hash_map_t[t[i]]:
                return False

        return True



if __name__ == "__main__":
    sol = Solution()
    # print(sol.isIsomorphic(s = "badc", t = "baba"))
    # print(sol.isIsomorphic(s = "BBBAAABA", t = "AAABBBBA"))
    print(sol.isIsomorphic(s = "egg", t = "add"))
    print(sol.isIsomorphic(s = "f11", t = "b23"))
    print(sol.isIsomorphic(s = "paper", t = "title"))
   
