class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for char in s:
                freq[ord('a') - ord(char)] += 1

            freq_map[tuple(freq)].append(s)

        print(freq_map)
        res = []
        for key, list_val in freq_map.items():
            res.append(list_val)

        return res