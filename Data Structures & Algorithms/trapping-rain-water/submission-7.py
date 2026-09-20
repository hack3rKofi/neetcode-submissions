class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        #Step 1: Initialize arrays
        maxLeft = [0] * n
        maxRight = [0] * n

        maxLeft[0] = height[0]
        maxRight[n-1] = height[n-1]

        #Step 3: Fill maxLeft
        for i in range(1, n):
            maxLeft[i] = max(height[i], maxLeft[i-1])
        
        #Step 3: Fill maxRight
        for i in range(n-2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i+1])
        
        #Step 4: Calculate Trapped Water
        water = 0

        for i in range(n):
            water += max(0,min(maxLeft[i],maxRight[i])-height[i])
        
        return water
