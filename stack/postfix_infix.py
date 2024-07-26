

def is_operand(x):
    if ('a' <= x <= 'z') or ('A' <= x <= 'Z'):
        return True
    return False

def postfix_to_infix(postfix_expr):
    # Initialize stack
    stack = []
    for i in postfix_expr:
        if is_operand(i):
            stack.insert(0, i)
        else:
            # symbol is operator
            op1 = stack.pop(0)
            op2 = stack.pop(0)
            construct_infix = "(" + op2 + i + op1 + ")"
            stack.insert(0, construct_infix)
    return stack[0]

postfix_expr = "ab*c+"
print(postfix_to_infix(postfix_expr))
# ((a*b)+c)