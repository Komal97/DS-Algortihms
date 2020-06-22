'''
Convert infix to postfix
Input: a+b*c-d/e 
Output: abc*+de/-
'''
# As soon as operand is encounter, append in output and keep a stack and push operators and append operators in output according to precedence
def isOperand(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/':
        return False
    return True

def precedence(ch):
    
    if ch == '*' or ch == '/':
        return 2
    elif ch == '+' or ch == '-':
        return 1
    return 0

def infix_to_postfix(infix):
    postfix = ''
    i = 0
    n = len(infix)
    stack = []
    while i<n:
        ch = infix[i]
        if isOperand(ch):
            postfix += ch
            i += 1
        else:
            if len(stack) == 0 or precedence(ch) > precedence(stack[-1]):
                stack.append(ch)
                i += 1
            else:
                postfix += stack.pop()
    while len(stack) > 0:
        postfix += stack.pop()
    print(postfix)

if __name__ == '__main__':
    infix = input()
    infix_to_postfix(infix)