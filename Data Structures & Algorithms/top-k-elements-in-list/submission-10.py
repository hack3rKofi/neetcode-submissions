class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_map = defaultdict(int)

        for n in nums:
            nums_map[n] += 1

        topk = sorted(nums_map.keys(), key=lambda x:nums_map[x], reverse=True)[:k]

        return topk        