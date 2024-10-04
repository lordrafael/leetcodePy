class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []

        for i in s:
            if i in bracket:
                stack.append(i)
            else:
                if len(stack) == 0 or i != bracket[stack.pop()]:
                    return False
            
        if len(stack) == 0:
            return True
        else:
            return False