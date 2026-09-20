class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numss = set(nums)
        longest  = 0


        for n in numss:
            if not n-1 in numss:
                length = 0

                while n + length in numss:
                    length += 1
                
                longest = max(length, longest)
        
        return longest