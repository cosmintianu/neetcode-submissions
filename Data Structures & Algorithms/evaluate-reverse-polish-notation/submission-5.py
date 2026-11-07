class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # print(stack)
            if t == '+' or t == '-' or t == '*' or t == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                res = 0
                match t:
                    case '+':
                        res = op1 + op2
                    case '-':
                        res = op1 - op2
                    case '*':
                        res = op1 * op2
                    case '/':
                        res = int(op1 / op2)
                print(op1, t, op2, res)

                stack.append(res)
            else:
                number = int(t)
                stack.append(number)

        return stack.pop()

        
