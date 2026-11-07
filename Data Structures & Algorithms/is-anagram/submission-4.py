class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for chars, chart in zip(s, t):
            count[chars] += 1
            count[chart] -= 1

        print(count)
        
        for char in count.values():
            if char != 0:
                return False


        return True
