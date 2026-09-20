class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        mul = 1

        for n in nums:
            prefix.append(mul)
            mul *= n
        
        suffix = []
        mul = 1

        for n in reversed(nums):
            suffix.append(mul)
            mul *= n
        
        suffix.reverse()

        res = []

        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
        

        return res