
def is_matching(a, b):
    if (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}'):
        return True
    else:
        return False
    
def is_balanced_parenthesis(expr):
    # Initialize stack
    stack = []

    for x in expr:
        # insert opening brackets into the stack
        if x in ['[', '(', '{']:
            stack.append(x)
        else:
            # No opening brackets availble in the expr
            if  not stack:
                return False
            else:
                # match x with top of stack
                if not is_matching(stack[-1], x):
                    return False
                else:
                    # remove last open bracket from stack
                    stack.pop()
    if stack:
        # this means still stack not empty
        return False
    else:
        return True

expr = "{({])}"
print(is_balanced_parenthesis(expr))