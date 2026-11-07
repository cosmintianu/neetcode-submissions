class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def comb(cur, i, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    return

                cur.append(nums[j])
                comb(cur, j, total + nums[j])
                cur.pop()

        comb([], 0, 0)
        return res
