class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                # print(ch)
                if ch in pairs and stack and stack[-1] == pairs[ch]:
                    stack.pop()
                    continue
                else:
                    return False

        return True if len(stack) == 0 else False