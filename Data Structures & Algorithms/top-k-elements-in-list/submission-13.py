class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
        
        topk = sorted(hashmap.keys(), key=lambda x:hashmap[x], reverse=True)[:k]

        return topk