class MinStack:

    def __init__(self):
        self.stack = []
        # self.min_value = float('infinity')
        # print(self.min_value)
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        # self.min_value = min(self.min_value, val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

m = MinStack()
