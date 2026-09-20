class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        
        count_t = Counter(t)
        count_s = Counter(s)

        for char in s:
            if count_t[char] != count_s.get(char, 0):
                return False

        return True        
        