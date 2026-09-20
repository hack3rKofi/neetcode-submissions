class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        multiplier = 1

        for n in nums:
            prefix.append(multiplier)
            multiplier *= n
        
        suffix = []
        multiplier = 1

        for n in reversed(nums):
            suffix.append(multiplier)
            multiplier *= n
        
        suffix.reverse()

        result = []

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        
        return result