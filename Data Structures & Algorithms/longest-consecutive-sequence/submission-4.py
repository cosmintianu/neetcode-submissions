class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        res = 0
        for num in num_set:
            if num - 1 not in num_set:
                l = 1            
                while num + l in num_set:
                    l += 1

                res = max(res, l)

        return res