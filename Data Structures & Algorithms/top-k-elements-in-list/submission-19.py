class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        topk = sorted(hashmap.keys(), key=lambda x:hashmap[x], reverse=True)[:k]

        return topk