class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, n in enumerate (nums):
            twosum = target - n

            if twosum in hashmap:
                return [hashmap[twosum], idx ]
            
            hashmap[n] = idx

        return []