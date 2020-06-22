'''
check paranthesis are redundant or not
Input: ((a+b)) + (c+d)
Output: Yes, redundant paranthesis
Input: (a+b) + (c+d)
Output: No, no redundant paranthesis
'''
from collections import deque
def redundant_paranthesis(expression):
    stack = deque()
    for ch in expression:
        if ch != ')':
            stack.append(ch)
        else:
            if stack[-1] == '(':
                return True
            else:
                while len(stack)>0 and stack[-1] != '(':
                    stack.pop()
                stack.pop()
    return False
    
if __name__ == '__main__':
    expression = input()
    print(redundant_paranthesis(expression))