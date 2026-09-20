class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        leftmax, rightmax = height[left], height[right]
        result = 0


        while left < right:
            if height[left] < height[right]:
                left += 1
                leftmax = max(height[left], leftmax)
                result += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(height[right], rightmax)
                result += rightmax - height[right]
        
        return result