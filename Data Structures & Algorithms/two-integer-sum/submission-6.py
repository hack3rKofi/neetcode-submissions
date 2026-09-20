class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            twoSum = target - n

            if twoSum in hashmap:
                return [hashmap[twoSum], i]

            hashmap[n] = i
        
        return []