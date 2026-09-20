class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charset = set()
        res = 0
        l = 0

        for idx, r in enumerate(s):
            while r in charset:
                charset.remove(s[l])
                l += 1
            charset.add(r)
            res = max(res, idx-l + 1 )

        return res