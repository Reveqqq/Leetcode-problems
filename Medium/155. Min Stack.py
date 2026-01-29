class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None
        


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(5)
    obj.push(-1)
    obj.push(3)
    obj.push(9)
    obj.push(-1)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

    print(obj.getMin())
    