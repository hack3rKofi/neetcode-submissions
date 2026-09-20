class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        unique = set(nums)

        for n in nums:
            if n-1 not in unique:
                count = 0

                while n + count in unique:
                    count += 1
                
                result = max(count, result)

        return result