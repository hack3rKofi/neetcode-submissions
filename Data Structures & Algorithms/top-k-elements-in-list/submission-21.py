class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = { n: nums.count(n) for n in nums}

        topk = sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)[:k]
        return topk