class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}


        for i, n in enumerate(nums):
            twosum = target - n

            if twosum in hashmap:
                return [hashmap[twosum], i]
            
            hashmap[n] = i
        
        return []