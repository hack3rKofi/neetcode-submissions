class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mynums = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i]-1 not in mynums:
                count = 0

                while count + nums[i] in mynums:
                    count += 1
                
                longest = max(count, longest)
        
        return longest