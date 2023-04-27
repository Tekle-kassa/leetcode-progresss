class MyQueue:

    def __init__(self):
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        if len(self.stack)==0:
            return False
        return self.stack.pop(0)
        

    def peek(self) -> int:
        if not self.stack:
            return False
        return self.stack[0]
        

    def empty(self) -> bool:
        if not self.stack:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()