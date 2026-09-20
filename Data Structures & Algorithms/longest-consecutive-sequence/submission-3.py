class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = set(nums)
        l = 0

        for i in n:
            if not i - 1 in n:
                j = 0

                while i + j in n:
                    j += 1
                
                l = max(j, l)
        
        return l