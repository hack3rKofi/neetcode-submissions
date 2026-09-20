class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        #Define the size of both leftMax and rightMax
        leftMax = [0] * n
        rightMax = [0] * n

        #Populate the initial first indices
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]

        #Start populating leftMax Array
        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i-1])
        
        #Start populating the rightMax Array
        for i in range(n-2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])

        #initialise the size of water to be stored
        water = 0

        for i in range(n):
            water += max(0, min(leftMax[i], rightMax[i])-height[i])

        return water                