class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] = -nums[k]
        res = []
        nums.sort()

        for i, nr in enumerate(nums):
            if nr > 0:
                break

            if i > 0 and nr == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nr + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum <0:
                    l += 1
                else:
                    res.append([nr, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res