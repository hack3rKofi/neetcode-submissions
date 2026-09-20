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
        res = []

        for i in range(len(nums)):
            res.append(p[i]*s[i])
        
        return res