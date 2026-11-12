class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        mp = {}
        res = 0

        while right < len(s):
            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)
            
            mp[s[right]] = right
            res = max(res, right - left + 1)
            right += 1



        return res

            
