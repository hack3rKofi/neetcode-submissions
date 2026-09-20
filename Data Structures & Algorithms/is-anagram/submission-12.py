class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_s = {}
        char_t = {}

        for c in s:
            char_s[c] = 1 + char_s.get(c, 1)
        
        for c in t:
            char_t[c] = 1 + char_t.get(c, 1)
        

        for c in s:
            if char_s[c] != char_t.get(c,0):
                return False
        
        return True