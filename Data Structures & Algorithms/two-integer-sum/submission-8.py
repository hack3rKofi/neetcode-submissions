class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, n in enumerate(nums):
            twoSum = target - n

            if twoSum in hashmap:
                return [hashmap[twoSum], idx]
            
            hashmap[n] = idx
        
        return -1