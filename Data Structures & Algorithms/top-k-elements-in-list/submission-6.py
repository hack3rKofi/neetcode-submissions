class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_n = {}

        for n in nums:
            count_n[n] = 1 + count_n.get(n, 0)
        
        topk = sorted(count_n.keys(), key=lambda x: count_n[x], reverse=True)[:k]

        return topk
