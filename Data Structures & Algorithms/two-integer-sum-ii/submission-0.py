class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        j, k = 0, len(nums) - 1
        while j < k:
            if nums[j] + nums[k] < target:
                j+= 1
                continue
            elif nums[j] + nums[k] > target:
                k -= 1
                continue
            else:
                return [j + 1 , k + 1]