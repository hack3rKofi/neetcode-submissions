class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p = []
        m = 1

        for n in nums:
            p.append(m)
            m *= n
        
        s = []
        m = 1

        for n in reversed(nums):
            s.append(m)
            m *= n
        
        s.reverse()
        r = []

        for i in range(len(nums)):
            r.append(s[i] * p[i])
        
        return r