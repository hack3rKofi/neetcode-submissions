class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {n: nums.count(n) for n in nums}

        topk = sorted(count, key=lambda x: count[x], reverse=True)[:k]

        return topk