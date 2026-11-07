class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()

        print(nums)

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            target = -nums[i]
            while j < k:
                print (i,j,k)
                if nums[j] + nums[k] < target:
                    j += 1
                    continue
                elif nums[j] + nums[k] > target:
                    k -= 1
                    continue
                else:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]]) 

                j, k = j + 1, k - 1


        return res