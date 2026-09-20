class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for idx, num in enumerate(nums):
            twosum = target - num

            if twosum in hashmap:
                return [hashmap[twosum], idx]
            else:
                hashmap[num] = idx
        
        return False