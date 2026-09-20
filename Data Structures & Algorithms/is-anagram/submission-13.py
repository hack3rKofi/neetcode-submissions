class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        count_t, count_s = {}, {}


        for i in s:
            count_s[i] = 1 + count_s.get(i, 0)
        
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        

        for i in s:
            if count_s[i] != count_t.get(i, 0):
                return False
        
        return True