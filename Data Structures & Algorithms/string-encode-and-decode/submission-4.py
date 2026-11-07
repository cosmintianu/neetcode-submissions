class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):

            number_str = ""
            while s[i] != '#':
                number_str += s[i]
                i += 1

            length = int(number_str)

            i += 1
            res. append(s[i:i+length])
            i+=length
        return res




