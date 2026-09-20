class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            twosum = target - nums[i]

            if twosum in hashmap:
                return [hashmap[twosum], i]
            
            hashmap[nums[i]] = i
        
        return []