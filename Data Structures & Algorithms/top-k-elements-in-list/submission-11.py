class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = defaultdict(int)

        for i in nums:
            n[i] += 1
        
        print(n)
        topk = sorted(n.keys(), key=lambda x: n[x], reverse=True)[:k]

        return topk