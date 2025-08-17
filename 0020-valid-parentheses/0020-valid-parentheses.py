from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            if len(stack)==0:
                return False
            else:
                if (char==')' and stack.pop()!='(') or (char==']' and stack.pop()!='[') or (char=='}' and stack.pop()!='{'):
                    return False
        if len(stack)==0:
            return True
        else:
            return False
