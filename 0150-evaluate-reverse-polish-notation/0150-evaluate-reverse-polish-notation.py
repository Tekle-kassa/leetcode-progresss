class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[] 
        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            else:
                second=stack.pop()
                first=stack.pop()
                if tokens[i]=='+':
                    res=(first)+(second)
                elif tokens[i]=='-':
                    res=(first)-(second)
                elif tokens[i]=='/':    
                    res=(first)/(second)
                    if res<0:
                        res=math.ceil(res)
                    else:
                        res=math.floor(res)
                elif tokens[i]=='*':
                    res=(first)*(second) 
                stack.append(res)
        return stack[0]
                
        