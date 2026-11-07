class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        l, r = 0, 0

        currSet = set()

        while r < len(s):
            currSeq = s[l:r]
            print(currSeq)
            if s[r] not in currSet:
                currSet.add(s[r])
                r += 1
                res = max(res, len(currSet))
            else:
                while s[r] in currSet:
                    currSet.remove(s[l])
                    l += 1
                
        return res
        