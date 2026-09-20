class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        dict_t = {}
        dict_s = {}

        for char in t:
            dict_t[char] = 1 + dict_t.get(char,0)
        
        for char in s:
            dict_s[char] = 1 + dict_s.get(char, 0)
        
        for char in s:
            if dict_s[char] != dict_t.get(char, 0):
                return False

        return True 