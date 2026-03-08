class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                second=stack.pop()
                first=stack.pop()
                if i == '+':
                    stack.append(first+second)
                elif i=='*':
                    stack.append(first*second)
                elif i =='/':
                    stack.append(int(first/second))
                else:
                    stack.append(first-second)
        return stack[0] 