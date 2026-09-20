class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)

        for n in s:
            hashmap_s[n] += 1
        

        for n in t:
            hashmap_t[n] += 1

        for i in s:
            if hashmap_s[i] != hashmap_t.get(i, 0):
                return False
        
        return True