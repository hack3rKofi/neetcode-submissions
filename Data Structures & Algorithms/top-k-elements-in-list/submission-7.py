class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}


        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        topk = sorted(count.keys(), key=lambda x:count[x], reverse=True)[:k]

        return topk