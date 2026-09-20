class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashset = {}

        for idx, num in enumerate(nums):
            twoSum = target - num

            if twoSum in hashset:
                return [hashset[twoSum], idx]
            
            hashset[num] = idx
        
        return False