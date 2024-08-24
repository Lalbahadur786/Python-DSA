def prec(c):
        if c == '^':
            return 3
        elif c == '*' or c == '/':
            return 2
        elif c == '+' or c == '-':
            return 1
        else:
            return -1
    
def associativity(c):
    if c == '^':
        return 'R'
    return 'L'
    
#Function to convert an infix expression to a postfix expression.
def InfixtoPostfix(exp):
    #code here
    stack = []
    result = []
    for i in range(len(exp)):
        c = exp[i]
        # put oprends in the result
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            result.append(c)
        
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop() # pop ) from stack
        else:
            while stack and (prec(c) < prec(stack[-1]) or prec(c) == prec(stack[-1])):
                result.append(stack.pop())
            stack.append(c)

    
    while stack:
        result.append(stack.pop())
    
    return "".join(result)

expr = "a+b*(c^d-e)^(f+g*h)-i"
print(InfixtoPostfix(expr))
