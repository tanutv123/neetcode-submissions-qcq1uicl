class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if self.min > val:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        if not self.stack:
            return 0
        top = self.stack[-1]
        if top > 0:
            return self.min + top
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min
        
