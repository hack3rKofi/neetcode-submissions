class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        multiplier = 1
        prefix = []

        for n in nums:
            prefix.append(multiplier)
            multiplier *= n
        
        multiplier = 1
        suffix = []

        for n in reversed(nums):
            suffix.append(multiplier)
            multiplier *= n
        
        suffix.reverse()
        results = []

        for n in range(len(nums)):
            results.append(prefix[n] * suffix[n])
        
        return results
        