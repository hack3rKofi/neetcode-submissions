class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsset = set(nums)
        longest = 0

        for n in numsset:
            if n - 1 not in numsset:
                count = 0

                while n + count in numsset:
                    count += 1
                
                longest = max(count, longest)
        
        return longest