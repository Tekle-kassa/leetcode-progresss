class MinStack:

    def __init__(self):
        self.arr=[]
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        
        

    def pop(self) -> None:
        if len(self.arr)==0:
            return False
        return self.arr.pop()
        

    def top(self) -> int:
        if len(self.arr)==0:
            return False
        return self.arr[len(self.arr)-1]
        

    def getMin(self) -> int:
        if len(self.arr)==0:
            return False
        return min(self.arr)
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()