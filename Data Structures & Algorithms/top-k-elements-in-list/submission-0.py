class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_nums = {}

        for n in nums:
            count_nums[n] = count_nums.get(n, 0) + 1
        
        topk = sorted(count_nums, key= lambda x: count_nums[x], reverse=True)[:k]
    
        return topk
        