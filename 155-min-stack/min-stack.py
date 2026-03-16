class MinStack:

    def __init__(self):
      self.st=[]
      self.mi=[]
    def push(self, val: int) -> None:
       self.st.append(val)
       if (len(self.mi) == 0 or val <= self.mi[-1]):
          self.mi.append(val) 
         
    def pop(self) -> None:
        if len(self.st)>0 :
            if self.st[-1] == self.mi[-1]:
                self.mi.pop()
        self.st.pop()
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mi[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()