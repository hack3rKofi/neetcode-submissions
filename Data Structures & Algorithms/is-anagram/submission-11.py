class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False


        count_s = {}
        count_t = {}

        for n in s:
            count_s[n] = 1 + count_s.get(n, 0)
        
        for n in t:
            count_t[n] = 1 + count_t.get(n, 0)
        
        for n in s:
            if count_s[n] != count_t.get(n, 0):
                return False
        
        return True