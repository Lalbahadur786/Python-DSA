

def is_operator(sym):
    operators_list = ['^', '*', '/', '-', '+', '(', ')']
    if sym in operators_list:
        return True
    return False

def prefix_to_infix(prefix_expr):
    # Initialize stack
    stack = []

    # read symbols from end
    i = len(prefix_expr) - 1
    while i >= 0:
        # check if symbol is oprend
        if not is_operator(prefix_expr[i]):
            stack.append(prefix_expr[i])
        else:
            # symbol is operator
            construct_expr = "(" + stack.pop() + prefix_expr[i] + stack.pop() + ")"
            stack.append(construct_expr)
        i -= 1

    return stack.pop()

prefix_expr = "*-A/BC-/AKL"
print(prefix_to_infix(prefix_expr))
# ((A-(B/C))*((A/K)-L))