class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftprod = []
        mul = 1

        for n in nums:
            leftprod.append(mul)
            mul *= n
        
        rightprod = []
        mul = 1

        for n in reversed(nums):
            rightprod.append(mul)
            mul *= n
        
        rightprod.reverse()

        result = []

        for i in range(len(nums)):
            result.append(leftprod[i] * rightprod[i])
        
        return result