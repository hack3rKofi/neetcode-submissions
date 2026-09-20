class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        left = []
        mul = 1

        for n in nums:
            left.append(mul)
            mul *= n

        
        right = []
        mul = 1

        for n in reversed(nums):
            right.append(mul)
            mul *= n
        
        right.reverse()
        result = []

        for i in range(len(nums)):
            result.append(left[i]*right[i])
        
        return result