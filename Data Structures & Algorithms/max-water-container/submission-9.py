class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        maxArea = 0


        while left < right:
            area = (right-left)*min(heights[left], heights[right])
            
            maxArea = max(area, maxArea)

            if heights[left] > heights[right]:
                right -= 1
            
            else:
                left += 1
        
        return maxArea