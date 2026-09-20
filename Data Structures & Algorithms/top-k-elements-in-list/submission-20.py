class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}

        for n in nums:
            h_map[n] = h_map.get(n, 0) + 1
        
        topk = sorted(h_map.keys(), key=lambda x:h_map[x], reverse=True)[:k]

        return topk
    