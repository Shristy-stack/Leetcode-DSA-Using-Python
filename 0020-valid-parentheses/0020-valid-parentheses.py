from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')':'(','}':'{',']':'[','>':'<'}
        for i in s:
            if i in '({[<':
                stack.append(i)
            elif i in ')}]>':
                if len(stack)==0 or stack.pop()!=pairs[i]:
                    return False

        return len(stack)==0