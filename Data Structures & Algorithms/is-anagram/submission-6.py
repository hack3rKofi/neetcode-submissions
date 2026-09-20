class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for char in s:
            count_s[char] += 1
        
        for char in t:
            count_t[char] += 1
        
        for i in s:
            if count_s[i] != count_t.get(i, 0):
                return False
        
        return True

