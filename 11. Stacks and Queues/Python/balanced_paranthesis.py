'''
input: (A+B) + (C+d)
output: True/False (tell whether paranthesis are balanced or not)
'''

def balanced_paranthesis(expression):
    
    stack = []
    for ch in expression:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0 or stack[-1]!='(':
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == '__main__':
    exp = input() 
    print(balanced_paranthesis(exp))