class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                i = 1
                while num + i in num_set:
                    i += 1

                res = max(res, i)


        return res