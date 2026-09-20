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
        result = []

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        
        return result