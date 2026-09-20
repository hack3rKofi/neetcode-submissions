class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            
            if n > 0:
                break
            
            l2,l3 = i+1, len(nums)-1

            while l2 < l3:
                threesum = n + nums[l2] + nums[l3]

                if threesum > 0:
                    l3 -= 1
                
                elif threesum < 0:
                    l2 += 1
                
                else:
                    result.append([n, nums[l2], nums[l3]])
                    l2 += 1
                    l3 -= 1

                    while l2 < l3 and nums[l3] == nums[l3+1]:
                        l3 -= 1
                    
                    while l2 < l3 and nums[l2] == nums[l2-1]:
                        l2 += 1
        return result