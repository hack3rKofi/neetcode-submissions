class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            if not n-1 in numset:
                l = 1

                while n + l in numset:
                    l += 1
                
                longest = max(l, longest)
        
        return longest