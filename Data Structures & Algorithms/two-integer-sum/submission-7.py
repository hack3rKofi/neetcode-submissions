class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nn = {}

        for idx, n in enumerate(nums):
            twoSum = target - n

            if twoSum in nn:
                return [nn[twoSum], idx]
            
            nn[n] = idx
        
        return []