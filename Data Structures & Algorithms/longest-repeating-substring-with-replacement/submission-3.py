class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = 0
        maxf = 0
        l = 0


        for idx, r in enumerate(s):
            count[r] = 1 + count.get(r, 0)
            maxf = max(count[r], maxf)

            if (idx-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, idx-l + 1)

        return res