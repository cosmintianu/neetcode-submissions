class Solution:
    from collections import defaultdict

    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_set = defaultdict(int)

        for c in p:
            p_set[c] += 1

        res = []

        l, r = 0, len(p)

        # baca
        # l = 0, r = 1 ba

        while r <= len(s):
            # print(s[l:r])
            new_hmap = defaultdict(int)

            for char in s[l:r]:
                new_hmap[char] += 1

            # print(new_hmap)
            # print(new_hmap == p_set)
            if new_hmap == p_set:
                res.append(l)

            l, r = l + 1, r + 1

        return res

