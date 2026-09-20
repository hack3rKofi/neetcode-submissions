class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for idx, num in enumerate(nums):
            twoSum = target - num

            if twoSum in hashmap:
                return [hashmap[twoSum], idx]
            
            hashmap[num] = idx
        
        return False