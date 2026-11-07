class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_present = set()

        for num in nums:
            if num in already_present:
                return True
            already_present.add(num)

        return False