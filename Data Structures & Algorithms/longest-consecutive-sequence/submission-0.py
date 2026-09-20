class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsset = set(nums)
        maxcount = 0

        for n in nums:
            if n - 1 not in numsset:
                counter = 0
                current_num = n

                while current_num in numsset:
                    current_num += 1
                    counter += 1
                    
                
                maxcount = max(maxcount, counter)
        
        return maxcount