class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     
        count_nums = {}

        for n in nums:
            count_nums[n] = 1 + count_nums.get(n, 0)
        
        topk = sorted(count_nums, key= lambda x: count_nums[x], reverse=True)[:k]
        
        return topk