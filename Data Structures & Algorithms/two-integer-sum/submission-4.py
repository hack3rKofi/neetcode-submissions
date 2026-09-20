class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for idx, n in enumerate(nums):
            s = target - n
            
            if s in hashmap:
                return[hashmap[s], idx ]
            
            hashmap[n] = idx
        
        return hashmap.values()
