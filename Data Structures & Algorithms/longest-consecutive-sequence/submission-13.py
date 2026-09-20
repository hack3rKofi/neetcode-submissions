class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        result = 0

        for n in numset:
            if n - 1 not in numset:
                count = 0

                while n + count in numset:
                    count += 1
                
                result = max(result, count)
        
        return result