class Solution:
    def trap(self, height: List[int]) -> int:
        maxPrefix = [0] * len(height)
        maxSuffix = [0] * len(height)

        res = 0

        currHMax = 0
        for i, h in enumerate(height):
            maxPrefix[i] = currHMax
            currHMax = max(currHMax, height[i])

        currHMax = 0
        for i in range(len(height) - 1, -1, -1):
            maxSuffix[i] = currHMax
            currHMax = max(currHMax, height[i])

        for i, h in enumerate(height):

            currWater = min(maxPrefix[i], maxSuffix[i]) - height[i] 
            print(i, currWater)
            res += currWater if currWater > 0 else 0


        return res