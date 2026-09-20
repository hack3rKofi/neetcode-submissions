class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for idx, n in enumerate(nums):
            two_sum = target - n

            if two_sum in hashmap:
                return [hashmap[two_sum], idx]
            
            hashmap[n] = idx

        return False