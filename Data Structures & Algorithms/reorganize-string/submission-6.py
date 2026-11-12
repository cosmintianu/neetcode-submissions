class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1

        max_heap = [[-f, c] for c, f in freq.items()]
        heapq.heapify(max_heap)

        # print(max_heap)
        
        res = []
        prev = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            count += 1
            res.append(char)

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            if count < 0:
                prev = [count, char]
            
        return "".join(res) if len(res) == sum(freq.values()) else ""