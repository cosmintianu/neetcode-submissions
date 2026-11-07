class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        l, r = 0, 0

        cnt = defaultdict(int)
        maxf = 0

        while r < len(s):
            cnt[s[r]] += 1
            maxf = max(maxf, cnt[s[r]])

            while r - l + 1 - maxf > k:
                cnt[s[l]] -= 1
                l += 1 

            res = max(res, r - l + 1)

            r += 1
        return res