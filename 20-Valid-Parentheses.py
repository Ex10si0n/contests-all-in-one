'''
Algorithms: None
Efficiency: High
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif (stack[-1] == "(" and char == ")") or (stack[-1] == "{" and char == "}") or (stack[-1] == "[" and char == "]"):
                stack.pop()
            else:
                stack.append(char)
        return True if len(stack) == 0 else False
