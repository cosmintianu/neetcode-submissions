class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        arr = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for key, value in count.items():
            arr[value].append(key)

        res = []
        for i in range(len(arr) -1, -1, -1):
            for candidate in arr[i]:
                res.append(candidate)
                if len(res) == k:
                    return res

        return res


            
