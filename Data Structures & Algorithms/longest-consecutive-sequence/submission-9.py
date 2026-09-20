class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique_nums = set(nums)
        longest = 0
        
        for n in unique_nums:
            if n-1 not in unique_nums:
                count = 0

                while n + count in nums:
                    count += 1
                
                longest = max(longest, count)
        
        return longest