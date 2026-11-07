class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '[' or c =='{':
                stack.append(c)

            if c == ')' or c == ']' or c == '}':
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if (c == ')' and out != '(') or (c == ']' and out != '[') or (c == '}' and out != '{'):
                    return False

        if len(stack) >0:
            return False
        else:
            return True