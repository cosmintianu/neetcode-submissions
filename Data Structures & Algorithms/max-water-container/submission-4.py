class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        print(res)
        l,r = 0, len(heights) - 1

        while l < r:
            currWater = 0
            if heights[l] < heights[r]:
                currWater = heights[l] * (r - l)
                res = max(res, currWater)
                l += 1
            else:
                currWater = heights[r] * (r - l)
                res = max(res, currWater)
                r -= 1

        return res