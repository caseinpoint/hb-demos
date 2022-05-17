def check_parens(symbols):
    """Are parentheses balanced in expression?"""

    # use a list as a stack
    open_parens = []

    for i, char in enumerate(symbols):
        if char == '(':
            # push onto stack
            open_parens.append(i)

            # display open parentheses position
            print('open:')
            print(symbols)
            print(f'{" " * i}ᐃ\n')

        elif char == ')':
            if len(open_parens) == 0:
                # display close parentheses position
                print('close: [no matching open]')
                print(symbols)
                print(f'{" " * i}ᐃ\n')

                return False

            else:
                # pop from stack
                idx = open_parens.pop()

                # display matching parentheses
                print('match:')
                print(symbols)
                print(f'{" " * idx}ᐃ{" " * (i - idx - 1)}ᐃ\n')

    if len(open_parens) > 0:
        # display open parentheses position
        print('open: [no matching close]')
        print(symbols)
        print(f'{" " * open_parens.pop()}ᐃ\n')

        return False

    return True


def check_brackets(symbols):
    """Do all opening brackets have a matching close?"""

    # lookup closing symbol by opening symbol
    brackets = {'(': ')', '[': ']', '{': '}'}

    # use a list as a stack
    stack = []

    for char in symbols:
        if char in brackets:
            # push onto stack
            stack.append(char)

        elif char in brackets.values():
            if len(stack) == 0:
                return False

            # pop from stack
            open_symbol = stack.pop()

            # check if they match
            if brackets[open_symbol] != char:
                return False

    return len(stack) == 0
