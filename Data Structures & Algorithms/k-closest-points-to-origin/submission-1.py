class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = points

        heap.sort(key=lambda x: math.sqrt(math.pow(x[0] - 0, 2) + math.pow(x[1] - 0, 2)))

        return heap[:k]