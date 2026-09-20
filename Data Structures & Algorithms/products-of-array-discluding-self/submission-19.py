class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        prev = []
        m = 1

        for n in nums:
            prev.append(m)
            m *= n
        
        suffix = []
        m = 1

        for n in reversed(nums):
            suffix.append(m)
            m *= n
        
        suffix.reverse()
        ans = []

        for i in range(len(nums)):
            ans.append(prev[i]*suffix[i])

        return ans