class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:

            if not n-1 in num_set:
                l = 0

                while n + l in num_set:
                    l += 1

                longest = max(l, longest)

        return longest 