class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for item in nums:
            freq[item] = 1 + freq.get(item, 0)

        topk = sorted(freq.items(), key= lambda x:x[1], reverse=True)[:k]

        return [key for key, _ in topk]

    