class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break
            
            l, r = i+1, len(nums)-1

            while l < r:
                threesum = nums[i] + nums[l] + nums[r]

                if threesum < 0:
                    l += 1
                
                elif threesum > 0:
                    r -= 1
                
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return result