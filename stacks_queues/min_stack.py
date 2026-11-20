"""
🟡 Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in O(1).

Time:  O(1) for all operations
Space: O(n)
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.get_min())   # -3
    stack.pop()
    print(stack.top())       # 0
    print(stack.get_min())   # -2
