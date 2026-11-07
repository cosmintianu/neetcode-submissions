class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        print(nums)
        # num1 + num2 = -num3

        for idx, num in enumerate(nums):
            
            if num >0:
                break
            if idx > 0 and num == nums[idx-1]:
                continue

            # target = - num
            # targetid = idx
            l,r = idx + 1, len(nums) - 1


            while l < r:
                threesum = nums[l] + nums[r] + num
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    #  nums[l] + nums[r] == target:
                    # print(targetid, l, r)
                    candidate = [num, nums[l], nums[r]]
                    if candidate not in res: 
                        res.append(candidate)

                    l, r = l + 1, r - 1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        
        return res

            

