class MinStack:
    arr = []
    minimum = None
    length = 0
    last = None
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        if val != None:
            newArr = [*self.arr, val]
                
            if not self.length:
                self.minimum = val
            else:
                if val < self.minimum:
                    self.minimum = val
            self.length += 1
            self.arr = newArr
            self.last = val
        return TypeError

    def pop(self) -> None:
        self.length -= 1
        newArr = self.arr[:self.length]
        self.arr = newArr
        if len(newArr):
            self.last = newArr[-1]
            self.minimum = min(newArr)
        else:
            self.last = None
            self.minimum = None
        
    def top(self) -> int:
        return self.last

    def getMin(self) -> int:
        if self.length:
            return self.minimum
        return None
