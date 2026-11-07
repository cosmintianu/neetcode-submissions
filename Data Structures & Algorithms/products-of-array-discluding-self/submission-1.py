class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        left_prod = 1
        prefix = []

        for i in range(len(nums)):
            prefix.append(left_prod)
            left_prod *= nums[i]

        right_prod = 1
        suffix = []        

        for i in range(len(nums)-1,-1,-1):
            suffix.append(right_prod)
            right_prod *= nums[i]

        suffix.reverse()

        for i in range(len(nums)):
            res.append(suffix[i] * prefix[i])

        return res