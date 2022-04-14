class MinStack:
    stack = []
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        if val != None:
            self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) >= 1:
            return min(self.stack)
        return None
    
obj = MinStack()
print(obj.getMin())
print(obj.push(-1))
print(obj.top())
print(obj.getMin())