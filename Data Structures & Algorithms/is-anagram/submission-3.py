class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        count_s = {}
        count_t = {}

        for c in s:
            count_s[c] = 1 + count_s.get(c, 0)
        
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        
        for char in s:
            if count_s[char] != count_t.get(char, 0):
                return False
        
        return True
        