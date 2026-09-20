class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        result = 0

        for n in nums:
            if n-1 not in numsset:
                count = 0

                while n + count in numsset:
                    count += 1

                result = max(count, result)


        return result 