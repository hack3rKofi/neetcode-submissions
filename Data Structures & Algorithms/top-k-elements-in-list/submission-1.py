class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        topk = Counter(nums).most_common(k)

        return [ele for ele, _ in topk]