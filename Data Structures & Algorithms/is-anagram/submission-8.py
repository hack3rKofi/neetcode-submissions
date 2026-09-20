class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        count_s = defaultdict(int)

        for i in s:
            count_s[i] += 1
        

        count_t = defaultdict(int)

        for j in t:
            count_t[j] += 1
        

        for i in s:
            if count_s[i] != count_t.get(i, 0):
                return False
        
        return True