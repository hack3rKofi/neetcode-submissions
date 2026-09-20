class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for idx, num in enumerate(nums):
            remainder = target - num

            if remainder in hashmap:
                return [hashmap[remainder], idx]
            
            else:
                hashmap[num] = idx
        
        return False