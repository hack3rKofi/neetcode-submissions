class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i, n in enumerate(nums):
            if n - 1 not in numset:
                count = 0

                while n + count in numset:
                    count += 1
                
                longest = max(count, longest)
        
        return longest
