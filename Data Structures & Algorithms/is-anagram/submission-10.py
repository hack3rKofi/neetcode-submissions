class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        count_t = {}
        count_s = {}

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
        for char in s:
            count_s[char] = 1 + count_s.get(char, 0)
        
        for char in count_t:
            if count_t[char] != count_s.get(char, 0):
                return False
        
        return True