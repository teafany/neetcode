class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.min_stk:
            prev_min = self.min_stk[-1]
            new_min = min(val, prev_min)
        else:
            new_min = val
        self.min_stk.append(new_min)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1] 

    def getMin(self) -> int:
        return self.min_stk[-1]