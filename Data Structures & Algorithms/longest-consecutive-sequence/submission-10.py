class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set(nums)

        longest = 0

        for n in unique:
            if n-1 not in unique:
                count = 0

                while n + count in unique:
                    count += 1
                

                longest = max(longest, count)


        return longest